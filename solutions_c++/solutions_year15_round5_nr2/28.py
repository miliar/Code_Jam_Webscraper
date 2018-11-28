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
#define fi first
#define se second
#define rep(i,n) for(int i = 0; i < n; ++i)
#define rrep(i,n) for(int i = 1; i <= n; ++i)
#define drep(i,n) for(int i = n-1; i >= 0; --i)
#define gep(i,g,j) for(int i = g.head[j]; i != -1; i = g.e[i].next)
#define each(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rng(a) a.begin(),a.end()
#define maxs(x,y) x = max(x,y)
#define mins(x,y) x = min(x,y)
#define pb push_back
#define sz(x) (int)(x).size()
#define pcnt __builtin_popcount
#define snuke srand((unsigned)clock()+(unsigned)time(NULL));
using namespace std;
typedef long long int ll;
typedef pair<int,int> P;
typedef vector<int> vi;
inline int in() { int x; scanf("%d",&x); return x;}
inline void priv(vi a) { rep(i,sz(a)) printf("%d%c",a[i],i==sz(a)-1?'\n':' ');}

const int MX = 100005, INF = 1000010000;
const ll LINF = 1000000000000000000ll;
const double eps = 1e-10;

int mod(int a, int m) {
  a %= m;
  a += m;
  return a%m;
}

struct Solver {
  void solve() {
    int n, m;
    cin >> n >> m;
    vi a(n-m+1);
    rep(i,n-m+1) cin >> a[i];
    vi l(m,0), r(m,0);
    rep(i,m) {
      int now = 0;
      for (int j = i+m; j < n; j += m) {
        now += a[j-m+1]-a[j-m];
        mins(l[i],now);
        maxs(r[i],now);
      }
    }
    int bi = 0, best = 0;
    rep(i,m) {
      int df = r[i]-l[i];
      if (df > best) {
        best = df;
        bi = i;
      }
    }
    int sl = 0, sr = 0;
    rep(i,m) {
      sl += (l[bi]-l[i]);
      sr += (r[bi]-r[i]);
    }
    int ans = 1;
    if (sr-sl+1 >= m) {
      ans = 0;
    } else {
      for (int i = sl; i <= sr; ++i) {
        if (mod(i,m) == mod(a[0],m)) ans = 0;
      }
    }
    ans += best;
    cout<<ans<<endl;
  }
};

int main(){
  int ts;
  scanf("%d",&ts);
  rrep(ti,ts) {
    Solver solver;
    printf("Case #%d: ",ti);
    solver.solve();
  }
  return 0;
}





