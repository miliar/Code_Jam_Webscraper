//bcw0x1bd2 {{{
#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
#define SZ(x) ((int)((x).size()))
#define ALL(x) begin(x),end(x)
#define REP(i,x) for (int i=0; i<(x); i++)
#define REP1(i,a,b) for (int i=(a); i<=(b); i++)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef long double ld;

#ifdef DARKHH
#define FILEIO(name)
#else
#define FILEIO(name) \
  freopen(name".in", "r", stdin); \
  freopen(name".out", "w", stdout);
#endif

#ifdef DARKHH
template<typename Iter>
ostream& _out(ostream &s, Iter b, Iter e) {
    s << "[ ";
    for ( auto it=b; it!=e; it++ ) s << *it << " ";
    s << "]";
    return s;
}
template<typename A, typename B>
ostream& operator << (ostream &s, const pair<A,B> &p) { return s<<"("<<p.first<<","<<p.second<<")"; }
template<typename T>
ostream& operator << (ostream &s, const vector<T> &c) { return _out(s,ALL(c)); }
template<typename T, size_t N>
ostream& operator << (ostream &s, const array<T,N> &c) { return _out(s,ALL(c)); }
template<typename T>
ostream& operator << (ostream &s, const set<T> &c) { return _out(s,ALL(c)); }
template<typename A, typename B>
ostream& operator << (ostream &s, const map<A,B> &c) { return _out(s,ALL(c)); }
#endif
// }}}
// Let's Fight! ~OAO~~

struct DisjointSet {
  int fa[105];
  void init() {
    REP(i,105) fa[i] = i;
  }
  int f(int x) { return x == fa[x] ? x : fa[x]=f(fa[x]); }
  void uni(int x, int y) {
    fa[f(y)] = f(x);
  }
}djs;

int N,R,C;
int love[105];
int at[105];
int table[105][105];

void input() {
  cin >> R >> C;
  N = 2*(R+C);
  REP(i,R+C) {
    int a,b;
    cin >> a >> b;
    love[a] = b;
    love[b] = a;
  }
}
void gen_table(int st) {
  int pos = 0;
  REP1(i,1,R) REP1(j,1,C){
    if (st & (1 << pos)) table[i][j] = 1;
    else table[i][j] = 0;
    pos++;
  }
}
int getA(int x, int y) {
  return (x-1)*(2*C+1)+y;
}
bool check(int st) {
  gen_table(st);
  //REP1(i,1,R) {
    //REP1(j,1,C) {
      //if (table[i][j] == 0) cout << "/";
      //else cout << "\\";
    //}
    //cout << endl;
  //}

  djs.init();
  REP1(i,1,R) REP1(j,1,C) {
    int a = getA(i,j);
    int b = a + C;
    int c = a + C + 1;
    int d = a + 2 * C + 1;
    if (table[i][j] == 0) {
      //cout << "UNION " << pii(a,b) << endl;
      //cout << "UNION " << pii(c,d) << endl;
      djs.uni(a,b);
      djs.uni(c,d);
    } else {
      //cout << "UNION " << pii(a,c) << endl;
      //cout << "UNION " << pii(b,d) << endl;
      djs.uni(a,c);
      djs.uni(b,d);
    }
  }
  REP1(i,1,N) {
    int x = at[i];
    int y = at[love[i]];
    if (djs.f(x) != djs.f(y)) {
      //cout << "FAIL @ " << i << " " << love[i] << endl;
      return false;
    }
  }
  return true;
}
void solve(int t) {
  int ans = -1;
  REP1(i,1,C) {
    at[i] = getA(1,i);
  }
  int p = 1;
  REP1(i,C+1,C+R) {
    at[i] = getA(p++,C)+C+1;
  }
  p = C;
  REP1(i,C+R+1,C+R+C) {
    at[i] = getA(R,p--)+2*C+1;
  }
  p = R;
  REP1(i,C+R+C+1,C+C+R+R) {
    at[i] = getA(p--,1)+C;
  }
  //REP1(i,1,N) cout << "at " << i << " : " << at[i] << endl;
  //REP1(i,1,N) cout << "LOVE " << i << " " << love[i] << endl;

  REP(i,1<<(R*C)) {
    if (check(i)) {
      ans = i;
      break;
    }
  }
  cout << "Case #" << t << ":" << endl;
  if (ans == -1) cout << "IMPOSSIBLE" << endl;
  else {
    gen_table(ans);
    REP1(i,1,R) {
      REP1(j,1,C) {
        if (table[i][j] == 0) cout << "/";
        else cout << "\\";
      }
      cout << endl;
    }
  }
}
int main() {
  IOS;
  int nT;
  cin >> nT;
  REP1(t,1,nT) {
    input();
    solve(t);
  }

  return 0;
}

