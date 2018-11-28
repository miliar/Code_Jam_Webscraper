#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>

#define rep(i,n) for (int n__=n,i=1;i<=n__;i++)
#define repb(i,b,n) for (int n__=n,i=b;i<=n__;i++)
using namespace std;
typedef long long LL;
const int mN=10000+50;

int a[mN];
int n,ma;
int count()
{
    int ct=0;
    rep(i,n)
        if (a[i]==ma)
            return ct;
        else
        {
            int cti1=0,cti2=0;
            rep(j,i-1)
                if (a[j]>a[i])
                    cti1++;
            repb(j,i+1,n)
                if (a[j]>a[i])
                    cti2++;
            ct+=min(cti1,cti2);
        }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int ta;
    cin>>ta;
    rep(tz,ta)
    {
        printf("Case #%d: ",tz);

        cin>>n;
        ma=0;
        rep(i,n)
        {
            cin>>a[i];
            if (a[i]>ma)
                ma=a[i];
        }
        int ans=0;
        ans+=count();
        rep(i,n/2)
        {
            int t=a[i];
            a[i]=a[n+1-i];
            a[n+1-i]=t;
        }
        ans+=count();
        printf("%d\n",ans);
    }

    return 0;
}
