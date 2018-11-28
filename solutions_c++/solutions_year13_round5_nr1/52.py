// Authored by dolphinigle
// GCJ 2013 3

#include <vector>
#include <list>
#include <map>
#include <set>

#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <assert.h>

#define FORN(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define REP(X,Y,Z) for (int (X) = (Y);(X) < (Z);++(X))

#define RE(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define FOR(X,Y,Z) for (int (X) = (Y);(X) <= (Z);++(X))

#define SZ(Z) ((int)(Z).size())
#define ALL(W) (W).begin(), (W).end()
#define PB push_back

#define MP make_pair
#define A first
#define B second

#define INF 1023123123
#define EPS 1e-11

#define MX(Z,Y) Z = max((Z),(Y))
#define MN(X,Y) X = min((X),(Y))

#define FORIT(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vint;

db best;
vector<ll> values;

int Test(int cnt, int winval, ll avail) {
  ll req = 0;
  int ok = 1;
  ll bets = 0;
  FORN(i, 37) {
    if (i < cnt) {
      // win
      if (values[i] > winval) {
        ok = 0;
        continue;
      }
      req += winval - values[i];
      bets += winval - values[i];
    } else {
      // lose
      if (values[i] > winval) continue;
      req += winval - values[i] + 1LL;
    }
  }
  if (req > avail) ok = 0;
  if (ok) {
    MX(best, 1.0 / (db)cnt * (db)bets * 36.0 - req);
  }
  return req <= avail;
}

int main() {
  int ntc;
  cin >> ntc;
  FORN(itc, ntc) {
    cout << "Case #" << (itc+1) << ": ";
    ll b, n;
    cin >> b >> n;
    values.clear();
    FORN(i, n) {
      ll x;
      cin >> x;
      values.PB(x);
    }
    for (int i = 0; i < 37-n; ++i) values.PB(0);
    sort(ALL(values));

    set<ll> important;
    FORIT(it, values) {
      important.insert(*it);
      important.insert(*it - 1);
      important.insert(*it + 1);
    }
    best = 0.0;
    for (int i = 1; i <= 37; ++i) {
      // i wins, 37-i loses
      FORIT(it, important) {
        if (*it <= 0) continue;
        Test(i, *it, b);
      }
      // bin search
      ll lb = 1;
      ll ub = 10000000000000LL;
      while (lb <= ub) {
        ll mid = (lb+ub)/2LL;
        if (Test(i, mid, b)) {
          lb = mid+1LL;
        } else {
          ub = mid-1LL;
        }
      }
    }
    printf("%.10lf\n", best);
  }
}
