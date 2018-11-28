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

struct Solver {
  int n;
  bool check(vvi a, vi used, vi us) {
    rep(i,n) {
      if (used[i]) continue;
      used[i] = 1;
      bool ex = false;
      rep(j,n) if (!us[j]) {
        if (a[i][j] == 0) continue;
        ex = true;
        us[j] = 1;
        if (!check(a, used, us)) return false;
        us[j] = 0;
      }
      if (!ex) return false;
      used[i] = 0;
    }
    return true;
  }
  int dfs(vvi a, int i, int j) {
    if (j == n) {
      j = 0;
      ++i;
    }
    if (i == n) {
      if (check(a,vi(n),vi(n))) return 0;
      return INF;
    }
    int res = dfs(a,i,j+1);
    if (a[i][j]) return res;
    a[i][j] = 1;
    mins(res, dfs(a,i,j+1)+1);
    a[i][j] = 0;
    return res;
  }
  void solve() {
    scanf("%d",&n);
    vvi a(n,vi(n));
    rep(i,n) {
      string s;
      cin >> s;
      rep(j,n) a[i][j] = s[j]-'0';
    }
    int ans = dfs(a,0,0);
    cout<<ans<<endl;
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





