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

int N;
int cnt[3];
pii frm[3];
static const char ch[3] = {'P','R','S'};

vector<int> go(int x, int rd) {
  if (rd >= N) {
    return {x};
  }
  vector<int> v1 = go(frm[x].F,rd+1);
  vector<int> v2 = go(frm[x].S,rd+1);
  if (v2 < v1) swap(v1,v2);
  v1.insert(end(v1),ALL(v2));
  return v1;
}

int main() {
  IOS;
  int nT;
  cin >> nT;
  REP1(t,1,nT) {
    cin >> N >> cnt[1] >> cnt[0] >> cnt[2];
    frm[0] = {0,1};
    frm[1] = {1,2};
    frm[2] = {0,2};
    vector<int> ans;
    REP(i,3) {
      vector<int> vec = go(i,0);
      int tmp[3] = {};
      for (auto it:vec) tmp[it]++;
      int flg = 1;
      REP(j,3) {
        if (tmp[j] != cnt[j]) {
          flg = 0;
          break;
        }
      }
      if (flg) {
        if (ans.empty() || vec < ans) ans = vec;
      }
    }
    if (ans.empty()) {
      cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    } else {
      cout << "Case #" << t << ": ";
      for (auto it:ans) {
        cout << ch[it];
      }
      cout << endl;
    }
  }


  return 0;
}

