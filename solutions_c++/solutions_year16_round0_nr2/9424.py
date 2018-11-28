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
string s;
void reverseit(ll x, ll y)
{
    while(true)
    {
        if(x > y) break;
        else
        {
            if(s[x] == '+') s[x] = '-';
            else s[x] = '+';
            if(x != y)
            {
                if(s[y] == '+') s[y] = '-';
                else s[y] = '+';
            }
        }
        swap(s[x], s[y]);
        x++; y--;
    }
}
int main()
{
    FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B-large.out", "w", stdout);
    ll t;
    cin >> t;
    ll k = 1;
    while(t--)
    {
        cin >> s;
        ll n = s.size();
        ll c = 0;
        for(ll i = n - 1; i; i--)
        {
            if(s[i] == '-')
            {
                if(s[0] == '+')
                {
                    c += 2;
                    f(j, i)
                    {
                        if(s[j] == '+')
                        {
                            s[j] = '-';
                        }
                        else
                        {
                            break;
                        }
                    }
                }
                else
                {
                    c++;
                }
                reverseit(0, i);
            }
        }
        if(s[0] == '-') c++;
        cout << "Case #" << k++ << ": " << c << "\n";
    }
    return 0;
}
