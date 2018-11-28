#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
//;
//;
#define sspeed ios_base::sync_with_stdio(0);cin.tie(0)
#define dbg(a) cout<<a<<endl
#define clr(a) memset(a,0,sizeof(a))
#define maxn 10001
#define mod 1000000007
#define eps 1e-9
#define inf 0x7fffffff
bool mark [11];
ll test (ll x)
{
    clr(mark);
    ll i;
    ll temp=0;
    ll cnt=0;
    for (i=1;i<=1000000&&cnt<10;i++)
    {
        temp += x;
        ll bit = 1;
//        cout<<i<<' '<<temp<<' '<<cnt<<endl;
        while (bit<=temp)
        {
//            cout<<(temp/bit)%10<<endl;
            if (mark[(temp/bit)%10]==0)
            {
                mark[(temp/bit)%10]=1;
                cnt++;
                if (cnt==10) return i;
            }
            bit*=10;
        }
//        cout<<cnt<<endl;
    }
    if (cnt==10) return i;
    else return 0;
}
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    ll i;
    int T;
    int caseno = 0;
    scanf("%d",&T);
    while (T--){
        scanf("%I64d",&i);
        ll ans = test(i);
        if (i==0)
            printf("Case #%d: INSOMNIA\n",++caseno);
        else printf("Case #%d: %I64d\n",++caseno,ans*i);
    }
    return 0;
}
