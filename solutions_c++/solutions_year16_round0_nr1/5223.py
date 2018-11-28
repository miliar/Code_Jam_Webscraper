#include<bits/stdc++.h>
using namespace std;
//-------------------------------------

#define ll long long
#define sc(x) scanf("%lld",&x)
#define sc2(x,y) scanf("%lld%lld",&x,&y)
#define sci(x) scanf("%d",&x)
#define sci2(x,y) scanf("%d%d",&x,&y)

#define mem(x) memset(x,0,sizeof x)
#define all(x) x.begin(),x.end()
#define pb(x)  push_back(x);
#define xx first
#define yy second
#define inf 999999999999999
#define mkp(x,y) make_pair(x,y)
#define pii pair<ll,ll>

//---------------------------------------

#define MX 200007
#define pi 2*acos(0.00)

#define open       freopen("input.in","r",stdin)
#define close      freopen ("output.txt","w",stdout)


int main()
{
    ll i, j, l, u, v, w, x, y, z, a, b, c, d, e, f, t = 1, tc;
    ll flg, sz, cnt, gt, ans, mx, mn;
    ll m, k, n,df;
    ll low, hi, md,vis[20];
    open;
    close;
    sc(tc);
    while(tc--)
    {
        sc(n);
        if(n==0)
        {
            printf("Case #%lld: INSOMNIA\n",t++);
            continue;
        }
        flg =0 ;
        for(i=0;i<=10;i++) vis[i]=0;
        for(i=1;i<=10000000;i++)
        {
            x = n*i,gt=1;
            while(x) vis[x%10]=1,x/=10;
            for(j=0;j<10;j++) gt*=vis[j];
            if(gt) flg=1;
            if(flg) break;
        }
        if(!flg) printf("Case #%lld: INSOMNIA\n",t++);
        else printf("Case #%lld: %lld\n",t++,i*n);
    }




    return 0;
}

