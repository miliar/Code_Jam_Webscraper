#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define fore(i,n) for(int i = 0; i< n ; i++ )
#define lop(i,n) for(int i = 1 ; i<=n ; i++ )
#define ops(i,n) for(int  i = n-1 ; i>=0 ; i-- )
#define forall( it,g )  for( typeof(g.begin()) it=g.begin();it!=g.end();it++ )
#define PI  3.141592653589793
#define mod  1000000007
#define inf 2000000000
#define INF -2000000000000000
#define modulo 1000000009
#define MH 1234533333333337
#define MH2 7779845079489377
#define enter endl
//ios_base::sync_with_stdio(0);cin.tie(0); cout.tie(0);
using namespace std;
typedef vector <int> vi;
typedef vector <vector <int> > vv;
typedef vector <pair <int,int > >vp;
typedef vector <vector <pair <int ,int > > > vvp;
typedef vector <pair <int ,pair <int ,int > > > vpp;
typedef pair<int,int> pp;
typedef long long ll;
typedef unsigned long long ull;
int n, k;
int p[] = {2, 3, 5, 7, 19, 29, 43, 101};
ll bs[11][20];
ll mulmod(ll a, ll b, ll m) {
    ll res = 0;
    while (a != 0) {
        if (a & 1) res = (res + b) % m;
        a >>= 1;
        b = (b << 1) % m;
    }
    return res;
}
ll power(ll base, ll p){
  ll ans = 1LL;
  ll mm = p;
  p--;
  while(p){
    if(p&1LL){
      ans = mulmod(ans, base,  mm);
    }
    base = mulmod(base, base, mm);
    p/=2;
  }
  return ans;
}
bool prime(ll m){
    if(m == 1)
    {
            return false;
    }
    fore(i, 8)
    {
            if(p[i] < m && power(p[i], m) != 1)
            {
                    return false;
            }
    }
    return true;
}
vector<ll> ans;
vector<vector<ll> > res;
void solve(ll x)
{
        vector<ll> a;
        for(int j = 2; j <= 10; j++)
        {
                ll alt = x;
                ll y = 0;
                int c = 0;
                while(alt)
                {
                        if(alt & 1)
                        {
                                y += bs[j][c];
                        }
                        alt /= 10;
                        c++;
                }
                if(prime(y))
                {
                        return;
                }
                a.pb(y);
        }
        res.pb(a);
        ans.pb(x);
        k--;
}
void gen(ll x, int len)
{
        if(k == 0)
        {
                return;
        }
        if(len == 1)
        {
                x = x * 10LL + 1;
                solve(x);
                return;

        }
        gen(x * 10LL, len - 1);
        gen(x * 10LL + 1, len - 1);
}
void calc()
{
        for(int j = 2; j <= 10; j++)
        {
                bs[j][0] = 1;
                lop(i, 19)
                {
                        bs[j][i] = bs[j][i - 1] * j;
                }
        }
}
ll fdiv(ll m)
{
        for(ll i = 2; i * i <= m; i++)
        {
                if(m % i == 0)
                {
                        return i;
                }
        }
}
int main()
{
    //ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    freopen("1.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    calc();
    int t, cases = 0;
    scanf("%d", &t);
    while(t--)
    {
            cases++;
            printf("Case #%d:\n", cases);
            scanf("%d %d", &n, &k);
            gen(1, n - 1);
            fore(i, ans.size())
            {
                    cout << ans[i] << " ";
                    vector<ll> a;
                    fore(j, res[i].size())
                    {
                            a.pb(fdiv(res[i][j]));
                    }
                    fore(j, a.size() - 1)
                    {
                            cout << a[j] << " ";
                    }
                    cout << a[8] << "\n";

            }
    }
    return 0;
}
