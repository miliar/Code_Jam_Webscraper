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
typedef vector<string> vs;
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

inline char rc(char c) { return c=='0'?'1':'0';}

struct Solver {
  void solve() {
    int n, m;
    scanf("%d%d",&n,&m);
    vs s(n); string t;
    rep(i,n) cin >> s[i];
    cin >> t;
    rep(i,n) {
      if (s[i] == t) {
        puts("IMPOSSIBLE");
        return;
      }
    }
    vs ans(2);
    rep(i,m) ans[0] += string(1,rc(t[i]))+"?";
    rep(i,m) ans[1] += string(1,rc(t[i]))+string(1,t[i]);
    ans[1] = ans[1].substr(0,sz(ans[1])-1);
    // rep(i,1<<m) {
    //   string x;
    //   rep(j,m) x += '0'+(i>>j&1);
    //   int k = 0;
    //   bool ok = true;
    //   rep(j,m) {
    //     if (x[j] == t[j]) {
    //       while (k < sz(ans[1]) && x[j] != ans[1][k]) ++k;
    //       if (k == sz(ans[1])) {
    //         ok = false;
    //         break;
    //       }
    //       ++k;
    //     }
    //   }
    //   if (ok != (x != t)) {
    //     cout<<"ng"<<" "<<x<<" "<<t<<endl;
    //     return;
    //   }
    // }
    cout<<ans<<endl;
    // cout<<"ok"<<endl;
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





