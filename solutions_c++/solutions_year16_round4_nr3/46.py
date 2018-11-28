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

const int di[] = {-1,0,1,0}, dj[] = {0,1,0,-1}; //^<v>

struct D {
  int i, j, v;
  D(int i, int j, int v):i(i),j(j),v(v) {}
  bool operator==(const D& a)const {
    return i==a.i&&j==a.j&&v==a.v;
  }
};

struct Solver {
  int h, w;
  D getpos(int i) {
    if (i < w) return D(0,i,2);
    i -= w;
    if (i < h) return D(i,w-1,3);
    i -= h;
    if (i < w) return D(h-1,w-1-i,0);
    i -= w;
    return D(h-1-i,0,1);
  }
  void solve() {
    scanf("%d%d",&h,&w);
    int n = (h+w)*2;
    vi a(n);
    rep(i,n/2) {
      int x, y;
      scanf("%d%d",&x,&y);
      --x; --y;
      a[x] = y;
      a[y] = x;
    }
    rep(si,n) {
      vi used(n,-1);
      stack<int> st;
      bool ok = true;
      vector<P> ps;
      rep(xi,n) {
        int i = (xi+si)%n;
        int x = a[i];
        if (used[x] == -1) {
          st.push(i);
          used[i] = sz(st);
        } else {
          if (used[x] != sz(st) || st.top() != x) {
            ok = false;
            break;
          }
          ps.pb(P(x,i));
          st.pop();
        }
      }
      if (!ok) continue;
      vvi d(h,vi(w));
      for (P p : ps) {
        D s = getpos(p.fi);
        D t = getpos(p.se); t.v ^= 2;
        // printf("%d %d %d\n",s.i,s.j,s.v);
        // printf("%d %d %d\n",t.i,t.j,t.v);
        int cnt = 0;
        while (1) {
          int i = s.i, j = s.j, v = s.v;
          if (i<0||j<0||i>=h||j>=w) {
            ok = false;
            break;
          }
          if (d[i][j]) s.v = v^d[i][j];
          else {
            s.v = (v+3)%4;
            d[i][j] = s.v^v;
          }
          if (s == t) break;
          s.i += di[s.v];
          s.j += dj[s.v];
          ++cnt;
          if (cnt >= h*w+5) {
            ok = false;
            break;
          }
        }
      }
      if (!ok) continue;
      rep(i,h) {
        string s;
        rep(j,w) {
          if (d[i][j] == 3) s += '\\';
          else s += '/';
        }
        cout<<s<<endl;
      }
      return;
    }
    cout<<"IMPOSSIBLE"<<endl;
  }
};

int main() {
  int ts;
  scanf("%d",&ts);
  rrep(ti,ts) {
    Solver solver;
    printf("Case #%d:\n",ti);
    solver.solve();
  }
  return 0;
}





