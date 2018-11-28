#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <string.h>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <numeric>
#include <cctype>
#include <bitset>
#include <cassert>
#define fi first
#define se second
#define rep(i,n) for(int i = 0; i < (n); ++i)
#define rrep(i,n) for(int i = 1; i <= (n); ++i)
#define drep(i,n) for(int i = (n)-1; i >= 0; --i)
#define gep(i,g,j) for(int i = g.head[j]; i != -1; i = g.e[i].next)
#define each(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rng(a) a.begin(),a.end()
#define maxs(x,y) x = max(x,y)
#define mins(x,y) x = min(x,y)
#define pb push_back
#define sz(x) (int)(x).size()
#define pcnt __builtin_popcount
#define snuke srand((unsigned)clock()+(unsigned)time(NULL));
#define df(x) int x = in()
#define dame { puts("0"); return 0;}
using namespace std;
typedef long long int ll;
typedef pair<int,int> P;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<P> vp;
inline int in() { int x; scanf("%d",&x); return x;}
inline void priv(vi a) { rep(i,sz(a)) printf("%d%c",a[i],i==sz(a)-1?'\n':' ');}
template<typename T>istream& operator>>(istream&i,vector<T>&v)
{for(T&x:v)i>>x;return i;}
template<typename T>string join(vector<T>&v)
{stringstream s;for(T&x:v)s<<' '<<x;return s.str().substr(1);}
template<typename T>ostream& operator<<(ostream&o,vector<T>&v)
{if(sz(v))o<<join(v);return o;}

const int MX = 100005, INF = 1001001001;
const ll LINF = 1e18;
const double eps = 1e-10;

const int C = 250;
double dp[205][505];

struct Solver {
  double f(vector<double> p) {
    int n = sz(p);
    rep(i,n+1)rep(j,505) dp[i][j] = 0;
    dp[0][C] = 1;
    rep(i,n) {
      rrep(j,500) {
        dp[i+1][j+1] += dp[i][j]*p[i];
        dp[i+1][j-1] += dp[i][j]*(1-p[i]);
      }
    }
    return dp[n][C];
  }
  void solve() {
    int n, m;
    scanf("%d%d",&n,&m);
    vector<double> p(n), d;
    rep(i,n) {
      scanf("%lf",&p[i]);
    }
    sort(rng(p));
    double ans = 0;
    rep(i,1<<n) {
      if (pcnt(i) != m) continue;
      d = vector<double>();
      rep(j,n) if (i>>j&1) d.pb(p[j]);
      maxs(ans, f(d));
    }
    printf("%.10f\n",ans);
  }
};

// struct Solver {
//   void solve() {
//     int n, m;
//     scanf("%d%d",&n,&m);
//     vector<double> p(n), d;
//     rep(i,n) {
//       scanf("%lf",&p[i]);
//     }
//     sort(rng(p));
//     rep(i,m/2) d.pb(p[i]);
//     rep(i,m/2) d.pb(p[n-1-i]);
//     rep(i,m+1)rep(j,505) dp[i][j] = 0;
//     dp[0][C] = 1;
//     rep(i,m) {
//       rrep(j,500) {
//         dp[i+1][j+1] += dp[i][j]*d[i];
//         dp[i+1][j-1] += dp[i][j]*(1-d[i]);
//       }
//     }
//     double ans = dp[m][C];
//     printf("%.10f\n",ans);
//   }
// };

int main() {
  int ts;
  scanf("%d",&ts);
  rrep(ti,ts) {
    Solver solver;
    printf("Case #%d: ",ti);
    solver.solve();
  }
  return 0;
}





