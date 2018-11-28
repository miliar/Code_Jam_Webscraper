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

int N,ip[105],nip[105];
string s;
int dp[2][105][105],dprev[2][105][105];

int go(int goal, int l, int r);
int go_rev(int goal, int l, int r);


int go_rev(int goal, int l, int r) {
  if (l == r) {
    return goal == nip[l] ? 0 : 1;
  }
  int &res = dprev[goal][l][r];
  if (res != -1) return res;
  res = 1029384756;
  if (nip[l] == goal) res = go_rev(goal,l+1,r);
  else res = min(res, go_rev(!goal,l+1,r)+1);
  if (nip[r] == goal) {
    res = min(res, 2+go(!goal,l,r-1));
  } else {
    res = min(res, 1+go(goal,l,r-1));
  }
  return res;
}
int go(int goal, int l, int r) {
  if (l == r) {
    return goal == ip[l] ? 0 : 1;
  }
  int &res = dp[goal][l][r];
  if (res != -1) return res;
  res = 1029384756;
  if (ip[r] == goal) res = go(goal,l,r-1);
  else res = go(!goal,l,r-1)+1;
  if (ip[l] == goal) {
    res = min(res, 2+go_rev(!goal,l+1,r));
  } else {
    res = min(res, 1+go_rev(goal,l+1,r));
  }
  return res;
}
int main() {
  IOS;
  int nT;
  cin >> nT;
  REP1(cas,1,nT) {
    cin >> s;
    N = SZ(s);
    REP(i,N) {
      ip[i] = s[i] == '+' ? 1 : 0;
      nip[i] = !ip[i];
    }
    memset(dp,-1,sizeof(dp));
    memset(dprev,-1,sizeof(dprev));
    int ans = go(1,0,N-1);
    cout << "Case #" << cas << ": " << ans << endl;
  }

  return 0;
}

