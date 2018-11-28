#include <bits/stdc++.h>
using namespace std;

#undef _P
#define _P(...) (void)printf(__VA_ARGS__)
#define FORR(x,arr) for(auto&& x:arr)
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define RFOR(i,a,b) for (int i = (b)-1; i >= (a); i--)
#define REP(i,n) for (int i = 0; i < (n); i++)
#define RREP(i,n) for (int i = (n)-1; i >= 0; i--)
#define ALL(x) (x).begin(), (x).end()
#define ITR(x,c) for(__typeof(c.begin()) x=c.begin();x!=c.end();x++)
#define RITR(x,c) for(__typeof(c.rbegin()) x=c.rbegin();x!=c.rend();x++)
#define BIT(n) (1LL<<(n))
#define SZ(x) ((int)(x).size())
typedef long long ll;
// -------------------------------------

int N, K;
double P[200];

template<class T> inline bool amax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }

void solve() {
  cin >> N >> K;
  REP(i, N) cin >> P[i];

  vector<int> m;
  double ma = 0;
  REP(i, BIT(N)) {
    if (__builtin_popcount(i) == K) {
      m.clear();
      REP(j, N) if (i & BIT(j)) {
        m.push_back(j);
      }

      double y = 0;
      double z = 0;
      REP(j, BIT(K)) {
        int h = __builtin_popcount(j);
        double p = 1.0;
        REP(k, K) {
          if (j & BIT(k)) {
            p *= P[m[k]];
          }
          else {
            p *= 1 - P[m[k]];
          }
        }
        if (h == K/2) y += p;
        z += p;
      }
      //_P("%d,%f,%f\n", i,y,z);
      amax(ma, y / z);
    }
  }

  _P("%.10f\n", ma);
}

int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  REP(i, T) {
    _P("Case #%d: ", i+1);
    solve();
  }

  return 0;
}
