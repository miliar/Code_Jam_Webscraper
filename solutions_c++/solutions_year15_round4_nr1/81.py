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

const int MX = 105, INF = 1000010000;
const ll LINF = 1000000000000000000ll;
const double eps = 1e-10;
const int di[] = {-1,0,1,0}, dj[] = {0,-1,0,1}; //^<v>
//const int di[] = {-1,0,1,-1,1,-1,0,1}, dj[] = {-1,-1,-1,0,0,1,1,1};


int h, w;
string s[MX];

struct Solver {
  bool ff(int i, int j, int v) {
    return f(i+di[v],j+dj[v],v);
  }
  bool f(int i, int j, int v) {
    if (i<0||j<0||i>=h||j>=w) return false;
    if (s[i][j] != '.') return true;
    return f(i+di[v],j+dj[v],v);
  }
  void solve() {
    cin >> h >> w;
    rep(i,h) cin >> s[i];
    int ans = 0;
    rep(i,h)rep(j,w) {
      if (s[i][j] == '.') continue;
      int nv = 0;
      if (s[i][j] == '^') nv = 0;
      if (s[i][j] == '<') nv = 1;
      if (s[i][j] == 'v') nv = 2;
      if (s[i][j] == '>') nv = 3;
      if (ff(i,j,nv)) continue;
      bool ok = false;
      rep(v,4) {
        if (ff(i,j,v)) ok = true;
      }
      if (!ok) {
        cout << "IMPOSSIBLE" << endl;
        return;
      }
      ans++;
    }
    cout<<ans<<endl;
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





