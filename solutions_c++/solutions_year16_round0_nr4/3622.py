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

#define MX 300007
#define pi 2*acos(0.00)

#define open       freopen("input.in","r",stdin)
#define close      freopen ("output.txt","w",stdout)


int main()
{
    ll i, j, l, u, v, w, x, y, z, a, b, c, d, e, f, tc;
    int cs=1;
    ll flg, sz, cnt, gt, ans, mx, mn;
    ll m, k, n,df;
    ll low, hi, md, sm, ff,tot,inp[200];

    freopen("input.in","r",stdin);
    freopen ("output.txt","w",stdout);
    sc(tc);
    while(tc--)
    {
        sc2(k,m);
        sc(z);
        cnt = 0;
        for(i=k; i>=1; i--)
        {
            inp[i]=cnt;
            cnt++;
        }
        tot = k;
        for(i=2; i<=m; i++)
        {
            tot=tot*k;
            for(j=1; j<=k; j++) inp[j]=inp[j]*k+(k-1);
        }

        printf("Case #%d:",cs++);
        for(i=1; i<=k; i++)
        {
            printf(" ");
            printf("%lld",tot-inp[i]);
        }
        printf("\n");
    }



    return 0;
}

