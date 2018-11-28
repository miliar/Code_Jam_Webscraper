#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pl;

#define sl(x) scanf("%I64d",&x)
#define pl(x) printf("%I64d\n",x)
#define sf(x) sort(x.begin(),x.end(),func)
#define s(x) sort(x.begin(),x.end())
#define pb push_back
#define all(v) v.begin(),v.end()
#define rs(v) { s(v) ; r(v) ; }
#define r(v) {reverse(all(v));}
#define mp make_pair
#define F first
#define S second
#define f(i,n) for(int i=0;i<n;i++)
#define rep(i,a,b) for(int i=a;i<=b;i++)

const ll mod = 1000000007;
const ll inf = LLONG_MAX;
const ll ninf = LLONG_MIN;
const ld eps = 1e-12;
const ll N = 1000005;
const ll M = 5005;
const ll LOGN = 19;

int main()
{
    FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
    ll t;
    cin >> t;
    ll k = 1;
    while(t--)
    {
        ll n;
        cin >> n;
        cout << "Case #" << k++ << ": ";
        if(n == 0)
        {
            cout << "INSOMNIA\n";
            continue;
        }
        ll m[10] = {};
        ll ans = 0;
        ll pre = n;
        for(ll i = 1; ;i++)
        {
            ll x = n * i;
            while(x)
            {
                m[x % 10] = 1;
                x /= 10;
            }
            pre = n * i;
            ll f = 0;
            for(ll j = 0; j <= 9; j++)
            {
                if(m[j] == 0)
                {
                    f = 1;
                    break;
                }
            }
            if(f == 0)
            {
                cout << pre << "\n";
                break;
            }
        }
    }
    return 0;
}
