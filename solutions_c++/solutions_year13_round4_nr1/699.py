#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <complex>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cmath>
#include <cassert>
#include <queue>
#include <set>
#include <map>
#include <valarray>
#include <bitset>
#include <stack>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define chmax(a,b) (a<(b)?(a=b,1):0)
#define chmin(a,b) (a>(b)?(a=b,1):0)
#define valid(y,x,h,w) (0<=y&&y<h&&0<=x&&x<w)
const int INF = 1<<29;
const double EPS = 1e-8;
const double PI = acos(-1);
typedef pair<int,int> pii;
typedef long long ll;

struct P {
  int x,p,f;
  bool operator<(const P &rhs) const {
    return x != rhs.x ? x < rhs.x : f < rhs.f;
  }
};

struct P2 {
  int s, p;
  bool operator<(const P2 &rhs) const {
    return s < rhs.s;
  }
};

const ll mod = 1000002013;

int main() {
  int T;
  cin >> T;
  REP(cs,T) {
    printf("Case #%d: ", cs+1);
    int n,m;
    cin >> n >> m;
    vector<P> v;
    ll ans = 0;
    REP(i,m) {
      int s, t, p;
      cin >> s >> t >> p;
      v.push_back((P){s,p,0});
      v.push_back((P){t,p,1});
      ll k = t-s;
      ans = (ans + k * (2*n+1-k)/2 % mod * p % mod ) % mod;
    }
    // cout << ans << endl;
    sort(ALL(v));
    ll sum = 0;
    priority_queue<P2> Q;
    FOR(it, v) {
      if (it->f) {
        while(Q.size() && it->p) {
          P2 p2 = Q.top(); Q.pop();
          int p = p2.p;
          ll t = min(p, it->p);
          ll k = it->x - p2.s;
          p2.p -= t;
          if (p2.p) {
            Q.push(p2);
          }
          it->p -= t;

          sum = (sum + k * (2*n + 1 - k) / 2 % mod * t % mod) % mod;
          // cout << it->x << " " << it->p << " " << p2.p << " " << t << " " << k << " " << sum << endl;
        }
      } else {
        Q.push((P2){it->x, it->p});
      }
    }
    // cout << ans << " " << sum << endl;
    ans = (ans - sum + mod) % mod;
    cout << ans << endl;
  }
}
