#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;

int check(LL n, LL r, LL t)
{
    LL x = 2*(n*r+n*(n-1))+n;
    return x<=t;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    LL r,t;
    while(T--)
    {
        scanf("%I64d%I64d",&r,&t);
        LL lo = 0, hi = t;
        while(lo+1 < hi)
        {
            LL mid = (lo+hi)/2;
            if(check(mid,r,t))lo = mid;
            else hi = mid;
        }
        printf("Case #%d: %I64d\n",++cas,lo);
    }
    return 0;
}
