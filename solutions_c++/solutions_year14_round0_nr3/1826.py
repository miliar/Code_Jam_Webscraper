import os
import sys
os.system("rm odp.out")
s = "./brut2 %s %d >> odp.out"
num = 1
with open(sys.argv[1]) as f:
    next(f);
    for line in f:
        if line != "\n":
            print (s%(line[:-1], num))
            os.system (s%(line[:-1], num))
            num = num + 1
