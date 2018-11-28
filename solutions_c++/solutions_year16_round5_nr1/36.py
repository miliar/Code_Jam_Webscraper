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

const int MX = 20005, INF = 1001001001;
const ll LINF = 1e18;
const double eps = 1e-10;

struct Solver {
  void solve() {
    string s;
    cin >> s;
    int n = sz(s);
    vi a(n);
    rep(i,n) a[i] = (s[i] == 'C');
    vvi dp(2,vi(1,-INF));
    dp[0][0] = dp[1][0] = 0;
    rep(i,n) {
      int m = sz(dp[0])+1;
      vvi p(2, vi(m, -INF));
      swap(dp, p);
      rep(j,2)rep(k,sz(p[j])) {
        maxs(dp[0][0], p[j][k]);
        maxs(dp[1][0], p[j][k]);
        maxs(dp[j^1][k+1], p[j][k]+(a[i]==j?0:5)-5);
        if (k) {
          maxs(dp[j^1][k-1], p[j][k]+(a[i]==j?5:0)+5);
          if (k == 1) maxs(dp[j][0], p[j][k]+(a[i]==j?5:0)+5);
        }
      }
      // rep(j,2) cout<<dp[j]<<endl;
    }
    int ans = dp[0][0];
    cout<<ans<<endl;
    // vvi dp(n, vi(n, -INF));
    // rep(i,n) dp[i][i] = -INF;
    // rep(i,n-1) dp[i][i+1] = (a[i]==a[i+1]?10:5);
    // rep(w,n) {
    //   if (w <= 1) continue;
    //   rep(l,n) {
    //     int r = l+w;
    //     if (r >= n) continue;
    //     for (int i = l; i < r; ++i) maxs(dp[l][r], dp[l][i]+dp[i+1][r]);
    //     maxs(dp[l][r], dp[l+1][r-1]+(a[l]==a[r]?10:5));
    //   }
    // }
    // // rep(i,n)for (int j = i; j < n; ++j) printf("%d %d %d\n",i,j,dp[i][j]);
    // vi d(n+1, -INF);
    // d[0] = 0;
    // rep(i,n) {
    //   rep(j,n) {
    //     if (i > j) continue;
    //     maxs(d[j+1], d[i]+dp[i][j]);
    //   }
    //   maxs(d[i+1], d[i]);
    // }
    // cout<<d[n]<<endl;
  }
};

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





