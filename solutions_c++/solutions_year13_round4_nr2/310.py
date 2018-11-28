#include <stdio.h>
#define MAX 53

typedef long long ll;

ll po[MAX];

int main()
{
    freopen("bin.txt","r",stdin);
    freopen("bout.txt","w",stdout);
    ll i,test,cas,n,p,lo,hi,mid,bef,no,a;
    po[0]=1;
    for (i=1;i<=50;i++) po[i]=po[i-1]*2;
    scanf("%lld",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%lld%lld",&n,&p);
        lo=0;
        hi=po[n]-1;
        while (lo<hi)
        {
            mid=(lo+hi+1)/2;
            for (i=0;i<=n&&po[i]-1<=mid;i++) ;
            i--;
            no=((po[i]-1)<<(n-i));
            if (no<p) lo=mid;
            else hi=mid-1;
        }
        a=lo;
        lo=0;
        hi=po[n]-1;
        while (lo<hi)
        {
            mid=(lo+hi+1)/2;
            for (i=0;i<=n&&po[i]-1<=po[n]-1-mid;i++) ;
            i--;
            if (po[n-i]-1<p) lo=mid;
            else hi=mid-1;
        }
        printf("Case #%lld: %lld %lld\n",cas,a,lo);
    }
    return 0;
}
