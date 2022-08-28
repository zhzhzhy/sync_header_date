import os
import subprocess
from datetime import datetime

print("------Date sycn from HTTP header start------")
#d = 'Sun, 28 Aug 2022 12:41:51 GMT'
#sdate = subprocess.check_output("curl -s --head http://baidu.com | grep ^Date: | sed 's/Date: //g'",shell=True).strip()
sdate = subprocess.check_output("curl -s --head http://baidu.com | grep ^Date: | sed 's/Date: //g'",shell=True).decode().strip()
print("original date RFC-2822 format for server: ",sdate)

os.system("echo '------Date convert start------'")
#os.system("echo "curl -s --head http://baidu.com | grep ^Date: | sed 's/Date: //g'")
#print(datetime.strptime(d, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d %H:%M:%S'))
#print("format to ISO-8601:")
new_date = datetime.strptime(sdate, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d %H:%M:%S')
print("format to ISO-8601:",new_date)

date_sync_cmd = "date -s '{0}'".format(new_date)
print("Date sync shell command: ",date_sync_cmd)
os.system(date_sync_cmd)
