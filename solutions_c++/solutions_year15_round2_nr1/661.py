#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <cmath>
#include <vector>
#include <string>
#include <iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;
long long res;
long long n,m;
long long Trans(long long x)
{
    long long tmp=0;
    while(x)
    {
        tmp=tmp*10LL+x%10LL;
        x/=10LL;
    }
    return tmp;
}
bool check0(long long x)
{
    int t=0;
    long long y=x;
    while(x) {t++;x/=10LL;}
    t=(t+1)/2;
    x=y;
    for(int i=0;i<t;i++)
    {
        if(x%10LL!=0) return false;
        x/=10LL;
    }
    return true;
}
bool check1(long long x)
{
    int t=0;
    long long y=x;
    while(x) {t++;x/=10LL;}
    t=(t+1)/2;
    x=y;
    if(x%10LL!=1LL) return false;
    x/=10LL;
    for(int i=1;i<t;i++)
    {
        if(x%10LL!=0) return false;
        x/=10LL;
    }
    return true;
}
long long work(long long x)
{
    int t=0;
    long long y=x;
    while(x) {t++;x/=10LL;}
    t=(t+1)/2;
    long long p=1;
    long long tmp=0;
    x=y;
    for(int i=0;i<t;i++)
    {
        tmp+=x%10LL*p;
        x/=10LL;
        p*=10LL;
    }
    res+=tmp-1LL;
    y-=tmp-1LL;
    return y;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    int cas=0;
    while(T--)
    {
        scanf("%lld",&n);
        res=1;
        while(n>1)
        {
            if(check0(n))
            {
                n--;
                res++;
            }
            else if(check1(n))
            {
                m = Trans(n);
                if( m == n) {n--;res++;}
                else {n=m;res++;}
            }
            else
            {
                n=work(n);
            }
        }
        printf("Case #%d: %lld\n",++cas,res);
    }

    return 0;
}
