// Authored by dolphinigle
// GCJ 2013 2

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

ll Best(ll n, ll p) {
 // cout << n << " " << p << endl;
  ll lb = 0;
  ll ub = (1LL << n) - 1LL;
  ll best = 0;
  ll tot = (1LL << n);

  while (lb <= ub) {
    ll mid = (lb+ub) / 2LL;
    // get best
    ll above = mid;
    ll under = tot - mid - 1LL;
    string me = "";
    while (above != 0LL || under != 0LL) {
      if (under == 0LL) {
        // can't win...
        me += 'L';
        above /= 2LL;
        continue;
      }
      me += 'W';
      under -= 1LL;
      ll nabove = above / 2LL;
      ll nunder = under / 2LL;
      if (above % 2LL) {
        nabove += 1LL;
      }
      above = nabove;
      under = nunder;
    }
   // cout << mid << " " << me << endl;
    ll value = 0LL;
    FORIT(it, me) {
      value *= 2LL;
      if (*it == 'L') {
        value += 1LL;
      }
    }
    if (value <= p) {
      best = mid;
      lb = mid+1LL;
    } else {
      ub=mid-1LL;
    }
  }
  return best;
}

int main() {
  int ntc;
  cin >> ntc;
  
  FORN(itc, ntc) {
    cout << "Case #" << (itc+1) << ": ";
    ll n, p;
    cin >> n >> p;
    if (p == (1LL << n)) {
      cout << (p-1LL) << " " << (p-1LL) << endl;
      continue;
    }
    p -= 1LL;
    //cout << n << " " << p << " ask " << endl;
    ll can_win = Best(n, p);
    ll border = Best(n, (1LL << n) - 2LL - p);
    border = (1LL << n) - border - 1LL;
    border -= 1LL;
    if (border < 0LL) border = 0LL;
    cout << border << " " << can_win << endl;
  }
  return 0;
}
