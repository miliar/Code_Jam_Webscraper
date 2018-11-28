#include <stdio.h>
#define MAX 100000000000000000LL

typedef long long ll;

int main()
{
    freopen("ain.txt","r",stdin);
    freopen("aout.txt","w",stdout);
    ll test,cas,r,t,lo,hi,mid,sum;
    scanf("%lld",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%lld%lld",&r,&t);
        lo=1;
        hi=MAX;
        while (lo<hi)
        {
            mid=(lo+hi+1)/2;
            sum=(4*r+2+(mid-1)*4)/2;
            if (sum>t/mid) hi=mid-1;
            else lo=mid;
        }
        printf("Case #%lld: %lld\n",cas,lo);
    }
    return 0;
}
