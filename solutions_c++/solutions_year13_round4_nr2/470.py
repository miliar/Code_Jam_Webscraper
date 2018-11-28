#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

long long n,tot,p;

bool check1(long long x)
{
    long long now=0,temp=tot;
    while(1)
    {
        if(x==1)
        {
            if(now<p)
                return 1;
            else
                return 0;
        }
        now=now+temp/2;
        temp/=2;
        x=(x-2)/2+1;
    }
}

bool check2(long long x)
{
    long long now=tot;
    while(1)
    {
        if(x==now)
        {
            if(now<=p)
                return 1;
            else
                return 0;
        }
        now=now/2;
        x=now-(now*2-x-1)/2;
    }
}

int main()
{
    freopen("2.in","r",stdin);
    freopen("2.txt","w",stdout);
    long long T,cas=0;
    scanf("%I64d",&T);
    while(T--)
    {
        scanf("%I64d%I64d",&n,&p);
        long long high=1,low=1,mid,i,ans1,ans2;
        for(i=1;i<=n;i++)
            high=high*2;
        tot=high;
        high=high+1;
        while(high-low>1)
        {
            mid=(high+low)/2;
            if(check1(mid))
                low=mid;
            else
                high=mid;
        }
        ans1=low;
        low=1;
        high=tot+1;
        while(high-low>1)
        {
            mid=(low+high)/2;
            if(check2(mid))
                low=mid;
            else
                high=mid;
        }
        ans2=low;
        printf("Case #%I64d: %I64d %I64d\n",++cas,ans1-1,ans2-1);
    }
    return 0;
}
