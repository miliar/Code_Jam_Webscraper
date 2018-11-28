#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

#define sspeed ios_base::sync_with_stdio(0);cin.tie(0)
#define dbg(a) cout<<a<<endl
#define clr(a) memset(a,0,sizeof(a))
#define maxn 10001
#define mod 1000000007
#define eps 1e-9
#define inf 0x7fffffff
ll quickpow (ll a,ll b)
{
    ll ans = 1;
    while (b--)
        ans*=a;
    return ans;
}
int main()
{
    freopen("in","r",stdin);
freopen("out","w",stdout);
    int T,caseno=0;
    int k,c,s;
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",++caseno);
        ll i;
        for (i=0;i<s;i++)
        {
            if (i) printf(" ");
            printf("%I64d",1ll+i*quickpow((ll)k,(ll)c-1));
        }
        printf("\n");
    }
    return 0;
}
