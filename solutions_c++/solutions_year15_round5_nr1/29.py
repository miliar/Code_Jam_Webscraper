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
typedef vector<vi> vvi;
inline int in() { int x; scanf("%d",&x); return x;}
inline void priv(vi a) { rep(i,sz(a)) printf("%d%c",a[i],i==sz(a)-1?'\n':' ');}

const int MX = 1000005, INF = 1000010000;
const ll LINF = 1000000000000000000ll;
const double eps = 1e-10;

struct Solver {
  int n, df;
  vi s, p, d;
  vvi to;
  void ins(vi& ar) {
    int x0, a, c, r;
    cin >> x0 >> a >> c >> r;
    rep(i,n) {
      ar.pb(x0);
      x0 = (x0*a+c)%r;
    }
  }
  void dfs(int v, int l=INF, int r=-INF) {
    queue<int> qv, ql, qr;
    qv.push(v);
    ql.push(l);
    qr.push(r);
    while (qv.size()) {
      v = qv.front(); qv.pop();
      l = ql.front(); ql.pop();
      r = qr.front(); qr.pop();
      mins(l,s[v]);
      maxs(r,s[v]);
      for (int u : to[v]) {
        // dfs(u,l,r);
        qv.push(u);
        ql.push(l);
        qr.push(r);
      }
      if (l+df>=r) {
        d[max(0,r-df)] += 1;
        d[l+1] -= 1;
      }
    }
  }
  void solve() {
    cin >> n >> df;
    ins(s);
    ins(p);
    rrep(i,n-1) p[i] %= i;
    to.resize(n);
    rrep(i,n-1) {
      to[p[i]].pb(i);
    }
    d = vi(MX,0);
    dfs(0);
    rep(i,MX-1) d[i+1] += d[i];
    int ans = 0;
    rep(i,MX) maxs(ans,d[i]);
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





