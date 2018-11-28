#include <cstdio>
#include <map>
using namespace std;
typedef long long ll;
const ll mod=1000002013;
map <ll,ll> in,out,here;
ll calc(ll n,ll num)
{
    return((n+(n-num+1))*num/2);
}
int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        ll n,m,ans;
        scanf("%lld%lld",&n,&m);
        ans=0;
        for (int i=1;i<=m;i++)
        {
            ll x,y,z;
            scanf("%lld%lld%lld",&x,&y,&z);
            in[x]+=z;
            out[y]+=z;
            ans=(ans+calc(n,y-x)*z)%mod;
        }
        while (!in.empty() || !out.empty())
            if (!in.empty() && in.begin()->first<=out.begin()->first)
            {
                here[-in.begin()->first]+=in.begin()->second;
                in.erase(in.begin());
            }
            else
            {
                while (1)
                {
                    ll now=min(out.begin()->second,here.begin()->second);
                    ans=(ans-calc(n,out.begin()->first+here.begin()->first)*now)%mod;
                    here.begin()->second-=now;
                    out.begin()->second-=now;
                    if (out.begin()->second==0)
                        break;
                    here.erase(here.begin());
                }
                out.erase(out.begin());
            }
        if (ans<0)
            ans+=mod;
        static int id=0;
        printf("Case #%d: %lld\n",++id,ans);
    }
    return(0);
}

