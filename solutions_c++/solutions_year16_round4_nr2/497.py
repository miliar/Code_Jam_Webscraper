#include <bits/stdc++.h>
using namespace std;


#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair
#define endl '\n'

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;

const int N = 420;

int n;
double p[N];

int act,nxt;
double dp[N][N];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    cout << fixed << setprecision(10);

    int ncas; cin >> ncas;
    forn(cas, ncas) {
        cout << "Case #" << cas+1 << ": ";

        int k; cin >> n >> k;
        forn(i,n) cin >> p[i];
        sort(p, p+n);


        double ans = 0;
        forn(pre, k+1) if (pre <= n) {
            int suf = k-pre;


            vector<double> ps;
            forn(i,pre) ps.pb(p[i]);
            forsn(i,n-suf,n) ps.pb(p[i]);

//            for (auto x : ps) D(x);

            fill(dp[0], dp[0]+n+2, 0);
            dp[0][0] = 1;
            forn(i,si(ps)) {
                forn(j,n+2) {
                    dp[i+1][j] = dp[i][j] * (1-ps[i]);
                    if (j) dp[i+1][j] += dp[i][j-1] * ps[i];
                }
            }
            ans = max(ans, dp[k][k/2]);
        }
        cout << ans << '\n';
    }
    return 0;
}
