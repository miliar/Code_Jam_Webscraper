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
#define double long double
using namespace std;
typedef long long int ll;
typedef pair<double, double> P;
typedef vector<int> vi;
inline int in() { int x; scanf("%d",&x); return x;}
inline void priv(vi a) { rep(i,sz(a)) printf("%d%c",a[i],i==sz(a)-1?'\n':' ');}

const int MX = 100005, INF = 1000010000;
const ll LINF = 1000000000000000000ll;
const double eps = 1e-13;

vector<P> p;
int n; double V, X;

struct Solver {
  bool f(double c) {
    double l = 0, r = 0;
    double x = V;
    rep(i,n) {
      double now = min(x,p[i].se*c);
      l += p[i].fi*now;
      x -= now;
    }
    reverse(rng(p));
    x = V;
    rep(i,n) {
      double now = min(x,p[i].se*c);
      r += p[i].fi*now;
      x -= now;
    }
    reverse(rng(p));
    // printf("%.10f %.10f (%.10f)\n", l, r, X);
    return (l-eps < X && X < r+eps);
  }
  void solve() {
    cin >> n >> V >> X;
    X *= V;
    p.clear();
    rep(i,n) {
      double v, x;
      cin >> v >> x;
      p.pb(P(x,v));
    }
    sort(rng(p));
    double l = 0, r = 1e10, c;
    rep(ti,200) {
      c = (l+r)/2;
      if (f(c)) r = c; else l = c;
    }
    if (r+1 > 1e10) {
      cout<<"IMPOSSIBLE"<<endl;
    } else {
      printf("%.18Lf\n", r);
    }
  }
};

int main(){
  int ts;
  scanf("%d",&ts);
  Solver solver;
  rrep(ti,ts) {
    printf("Case #%d: ",ti);
    solver.solve();
  }
  return 0;
}





