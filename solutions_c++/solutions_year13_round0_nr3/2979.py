#include <stdio.h>
#include <string.h>
#include <iostream>
#include <math.h>
using namespace std;

bool Check(long long t)
{
    long long k=t,ret=0;
    while(k)
    {
        ret=ret*10+k%10;
        k/=10;
    }
    if (ret!=t) return false;
    return true;
}

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int i,j,n,T,ans,cnt=1;
    long long x,y,tmp;
    scanf("%d",&T);
    while(T--)
    {
        cin>>x>>y;
        ans=0;
        for (i=sqrt(x*1.0);;i++)
        {
            tmp=i*i;
            if (tmp<x) continue;
            if (tmp>y) break;
            if (Check(i)==false) continue;
            ans+=Check(tmp);
        }
        printf("Case #%d: %d\n",cnt++,ans);
    }
    return 0;
}
