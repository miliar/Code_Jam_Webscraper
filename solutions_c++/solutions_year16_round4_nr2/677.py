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

typedef long double ld;
int N,K;
ld prob[205],dp[20][20];
ld ans;
vector<int> vec;

void input() {
  cin >> N >> K;
  REP(i,N) cin >> prob[i];
}
ld calc() {
  memset(dp,0,sizeof(dp));
  dp[0][0] = 1.0;
  REP1(i,1,K) {
    int id = vec[i-1];
    dp[i][0] = dp[i-1][0] * (1-prob[id]);
    REP1(j,1,i) {
      dp[i][j] = dp[i-1][j] * (1-prob[id]) + dp[i-1][j-1]*prob[id];
    }
  }
  //cout << vec << " " << dp[K][K/2] << endl;
  //for (auto it:vec) cout << prob[it] << endl;
  //REP1(i,0,K) {
    //REP1(j,0,i) cout << dp[i][j] << " ";
    //cout << endl;
  //}
  return dp[K][K/2];
}
void DFS(int cur) {
  if (cur >= N) {
    if (SZ(vec) == K) {
      ans = max(ans, calc());
    }
    return;
  }
  DFS(cur+1);
  vec.PB(cur);
  DFS(cur+1);
  vec.pop_back();
}
void solve(int t) {
  memset(dp,0,sizeof(dp));
  vec.clear();
  ans = 0;
  DFS(0);
  cout << "Case #" << t << ": " << fixed << setprecision(10) << ans << endl;
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

