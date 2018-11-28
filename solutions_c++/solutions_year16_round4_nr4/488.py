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

int N,ans,ip[5][5];
int bt[5][5];

void input() {
  cin >> N;
  REP(i,N) {
    string s;
    cin >> s;
    REP(j,N) ip[i][j] = s[j] - '0';
  }
}
void gen_bt(int st) {
  int pos = 0;
  REP(i,N) REP(j,N) {
    bt[i][j] = (st & (1<<pos)) ? 1 : 0;
    pos++;
  }
}
int calc(int st) {
  gen_bt(st);
  int res = 0;
  REP(i,N) REP(j,N) {
    if (ip[i][j] and !bt[i][j]) return N*N;
    if (!ip[i][j] and bt[i][j]) res++;
  }
  return res;
}
int flg;
int used[4];
int per[4];
void DFS(int i) {
  if (i >= N) {
    return;
  }
  int tot = 0;
  REP(j,N) {
    int id = per[i];
    if (used[j]) continue;
    if (!bt[id][j]) continue;
    tot++;
    used[j] = 1;
    DFS(i+1);
    used[j] = 0;
    if (flg) return;
  }
  if (!tot) flg = 1;
}
bool check(int st) {
  gen_bt(st);
  REP(i,N) per[i] = i;
  do {
    REP(i,N) used[i] = 0;
    flg = 0;
    DFS(0);
    if (flg) return false;
  } while (next_permutation(per,per+N));
  return true;
}
void solve(int t) {
  ans = N*N;
  REP(i,(1<<N*N)) {
    if (check(i)) {
      ans = min(ans, calc(i));
    }
  }
  cout << "Case #" << t << ": " << ans << endl;
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

