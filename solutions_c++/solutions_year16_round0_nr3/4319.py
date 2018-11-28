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

#define open       freopen("input.txt","r",stdin)
#define close      freopen ("output.txt","w",stdout)

ll gl;
ll cov(ll nbr,ll base)
{
    ll x = nbr,gt=0,pw=1,i;
    while(x)
    {
        if(x%2) gt+= pw;
        x/=2;
        pw*=base;
    }
    gl = gt;
    for(i=2; i*i<=gt; i++)
    {
        if(gt%i==0)
        {
            return i;
        }
    }
    return 0;
}

int main()
{
    ll i, j, l, u, v, w, x, y, z, a, b, c, d, e, f, t = 1, tc;
    ll flg, sz, cnt, gt, ans, mx, mn;
    ll m, k, n,df;
    ll low, hi, md, sm, ff;
//    cout<<cov(55,3)<<endl;
//    cout<<gl<<endl;
    open;
    close;
    sc(tc);
    while(tc--)
    {
        vector<ll> tk[202],val;

        sc2(n,m);
        ll id = 0;
        for(i=0; i<(1ll<<n); i++)
        {
            a = i;
            if( (a%2) && (a&(1<<(n-1))) )
            {
                for(j=2; j<=10; j++)
                {
                    gt = cov(i,j);
                    if(!gt) break;
                    tk[id].pb(gt);
                }
                if(tk[id].size()==9)
                {
                    val.pb(gl);
                    id++;
                }
                else tk[id].clear();
                if(id==m) break;
            }
        }
        printf("Case #%lld:\n",t++);
        for(i=0; i<m; i++)
        {
            printf("%lld ",val[i]);
            for(j=0; j<9; j++)
            {
                if(j) printf(" ");
                printf("%lld",tk[i][j]);
            }
            printf("\n");
        }
        printf("\n");

    }

    return 0;
}

