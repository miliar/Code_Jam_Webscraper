#include <bits/stdc++.h>
#define For(i,l,r) for (int i=l;i<=r;i++)
#define Rep(i,n) for(int i=0,n__=n;i<n__;i++)
using namespace std;
int a[1001];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int ta;
    cin>>ta;
    For(tz,1,ta)
    {
        int ans=1000;
        int n;
        cin>>n;
        For(i,1,n)
            cin>>a[i];
        For(t,1,1000)
        {
            int now=t;
            For(i,1,n)
                now+=(a[i]-1)/t;
            ans=min(ans,now);
        }
        printf("Case #%d: %d\n",tz,ans);
    }
}
