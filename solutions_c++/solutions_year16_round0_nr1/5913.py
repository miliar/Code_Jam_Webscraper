#include <bits/stdc++.h>
#define LL long long
using namespace std;

const int maxn = 1000000 + 10;

bool vis[10];

bool ok()
{
    for (int i=0;i<10;i++) if (!vis[i]) return 0;
    return 1;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas=0;
    LL n;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld",&n);
        memset(vis,0,sizeof vis);
        LL ans;
        for (LL i=1;i<=maxn;i++)
        {
            LL m = n * i;
            while(m)
            {
                vis[m % 10] = 1;
                m/=10;
            }
            if (ok())
            {
                ans = n * i; break;
            }
        }
        if (ok()) printf("Case #%d: %lld\n",++cas,ans);
        else printf("Case #%d: INSOMNIA\n",++cas);
    }
    return 0;
}
