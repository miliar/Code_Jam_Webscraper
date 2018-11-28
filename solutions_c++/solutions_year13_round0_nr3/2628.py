def sqrt(N):
    if N==0:
        return 0
    x=1
    NN=N
    while NN>=1:
        x*=4
        NN/=4
    while True:
        y = (x + N/x)/2
        if y >= x:
            return x
        x = y

t = int(raw_input())
print t
for i in range(t):
    a,b=map(int,raw_input().split())
    aa = sqrt(a)
    bb = sqrt(b)
    while aa*aa<a:
        aa+=1
    while aa>0 and (aa-1)*(aa-1)>=a:
        aa-=1
    while (bb+1)*(bb+1)<=b:
        bb+=1
    while bb>0 and bb*bb>b:
        bb-=1
    print aa-1,bb
