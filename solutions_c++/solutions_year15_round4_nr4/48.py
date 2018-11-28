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

const int MX = 100005, INF = 1000010000;
const ll LINF = 1000000000000000000ll;
const double eps = 1e-10;
const int di[] = {-1,0,1,0,0}, dj[] = {0,-1,0,1,0}; //^<v>
//const int di[] = {-1,0,1,-1,1,-1,0,1}, dj[] = {-1,-1,-1,0,0,1,1,1};

int r, c, ans;
vvi d;
set<vvi> mp;


struct Solver {
  inline bool f(int i, int j) {
    if (i<0||i>=r) return true;
    if (j < 0) j += c;
    if (j >= c) j -= c;
    if (d[i][j] == -1) return true;
    int a = 0, b = 0;
    rep(v,4) {
      int ni = i+di[v], nj = j+dj[v];
      if (ni<0||ni>=r) continue;
      if (nj < 0) nj += c;
      if (nj >= c) nj -= c;
      if (d[ni][nj] == -1) b++;
      else if (d[ni][nj] == d[i][j]) a++;
    }
    return (a <= d[i][j] && d[i][j] <= a+b);
  }
  void pri() {
    puts("---");
    rep(i,r) {
      rep(j,c) printf("%d ",d[i][j]);
      puts("");
    }
  }
  void add() {
    vvi a = d;
    rep(i,c) {
      rep(j,r) {
        d[j].pb(d[j][0]);
        d[j].erase(d[j].begin());
      }
      mins(a,d);
    }
    // if (mp.count(a) == 0 && r == 5 && c == 6) pri();
    mp.insert(a);
  }
  void dfs(int i, int j) {
    if (j == c) i++, j = 0;
    if (i == r) {
      // pri();
      add();
      return;
    }
    rrep(k,3) {
      d[i][j] = k;
      bool ok = true;
      rep(v,5) ok &= f(i+di[v],j+dj[v]);
      if (ok) dfs(i,j+1);
      d[i][j] = -1;
    }
  }
  void solve() {
    scanf("%d%d",&r,&c);
    ans = 0;
    d = vvi(r,vi(c,-1));
    mp.clear();
    dfs(0,0);
    cout<<sz(mp)<<endl;
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





