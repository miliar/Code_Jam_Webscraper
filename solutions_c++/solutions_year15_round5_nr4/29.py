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
typedef vector<ll> vll;
inline int in() { int x; scanf("%d",&x); return x;}
inline void priv(vi a) { rep(i,sz(a)) printf("%d%c",a[i],i==sz(a)-1?'\n':' ');}

const int MX = 100005, INF = 1000010000;
const ll LINF = 1000000000000000000ll;
const double eps = 1e-10;

void pri(vll& p) {
  rep(i,sz(p)) {
    cout<<p[i];
    if (i == sz(p)-1) cout << endl;
    else cout << " ";
  }
}

struct Solver {
  int n;
  bool del(vll& a, vll& c, map<ll,int>& mp, ll x) {
    if (x == 0) {
      rep(i,n) {
        if (c[i]&1) return false;
        c[i] /= 2;
      }
      return true;
    }
    rep(i,n) {
      if (a[i] < a[0]+x) continue;
      auto it = mp.find(a[i]-x);
      if (it == mp.end()) continue;
      c[i] -= c[it->se];
      if (c[i] < 0) return false;
    }
    return true;
  }
  vll solve2(vll a, vll c) {
    vll ans;
    map<ll,int> mp;
    ll l = -a[0];
    rep(i,n) a[i] += l;
    ll s = 0;
    rep(i,n) s += c[i];
    rep(i,n) mp[a[i]] = i;
    while (s>1) {
      // pri(a); pri(c);
      ll x;
      vector<ll> e;
      drep(i,n) if (c[i]) e.pb(a[i]);
      if (sz(e) == 1) {
        x = 0;
      } else {
        x = e[0]-e[1];
      }
      ans.pb(x);
      if (!del(a,c,mp,x)) return vll();
      s >>= 1;
    }
    return ans;
  }
  bool can(vll& p, ll s) {
    set<ll> x, y;
    x.insert(0);
    rep(i,sz(p)) {
      if (p[i] <= 0) continue;
      y = x;
      for (ll tx : y) x.insert(tx+p[i]);
    }
    return x.count(s) != 0;
  }
  void solve() {
    vll a, c;
    cin >> n;
    a.resize(n);
    c.resize(n);
    rep(i,n) cin >> a[i];
    rep(i,n) cin >> c[i];
    vll p = solve2(a,c);
    sort(rng(p));
    reverse(rng(p));
    ll s = -a[0];
    rep(i,sz(p)) {
      p[i] *= -1;
      s += p[i];
      if (can(p,s)) {
      } else {
        s -= p[i];
        p[i] *= -1;
      }
    }
    sort(rng(p));
    pri(p);
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





