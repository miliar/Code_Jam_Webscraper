#include<cstdio>
#include<cmath>
#include<iostream>
using namespace std;

int f[10000010];

bool isp(long long a)
{
    int digit[20],cnt=0;
    for (;a;a/=10) digit[cnt++]=a%10;
    for (int i=0;i<cnt;i++)
    if (digit[i]!=digit[cnt-1-i])
        return 0;
    return 1;
}

int main()
{
    for (int i=1;i<=10000000;i++)
        f[i]=f[i-1]+(isp(i) && isp((long long)i*i));
    int t=0,tot;
    for (scanf("%d",&tot);tot--;)
    {
        long long a,b;
        cin >> a >> b;
        a=(int)(sqrt(a-1)+1e-7);
        b=(int)(sqrt(b)+1e-7);
        printf("Case #%d: %d\n",++t,f[b]-f[a]);
    }

    
}
