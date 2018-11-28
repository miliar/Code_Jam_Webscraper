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

int d[][2] = {{0,1},{1,2},{2,0}};

int win(int a, int b) {
  if (a+b == 2) return 2;
  return min(a,b);
} 
struct Solver {
  vi dfs(vi a, vi o, int dep) {
    for (int i : a) if (i < 0) return {};
    vi res;
    if (dep == 0) {
      rep(i,3)rep(j,a[i]) res.pb(i);
      return res;
    }
    int sum = 0;
    rep(i,3) sum += a[i];
    sum /= 2;
    vi b;
    b.pb(sum-a[2]);
    b.pb(sum-a[0]);
    b.pb(sum-a[1]);
    vi r;
    r.pb(win(o[0],o[1]));
    r.pb(win(o[0],o[2]));
    r.pb(win(o[1],o[2]));
    vi x = dfs(b,r,dep-1);
    vi w(3);
    rep(i,3) w[o[i]] = i;
    for (int i : x) {
      int a = i, b = (i+1)%3;
      if (w[a] > w[b]) swap(a,b);
      res.pb(a);
      res.pb(b);
    }
    return res;
  }
  void solve() {
    int n;
    vi a(3);
    cin >> n;
    int n2 = 1<<n;
    cin >> a;
    swap(a[0],a[1]);
    vi x = dfs(a,{0,1,2},n);
    if (sz(x) == 0) {
      cout<<"IMPOSSIBLE"<<endl;
      return;
    }
    string s, t = "PRS";
    for (int i : x) s += t[i];
    cout<<s<<endl;
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





