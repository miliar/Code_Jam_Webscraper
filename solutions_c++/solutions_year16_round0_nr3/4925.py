#include <assert.h>
#include <memory.h>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define pb push_back
#define INF 1011111111
#define FOR(i, a, b) for (int _n(b), i(a); i < _n; i++)
#define rep(i, n) FOR(i, 0, n)
#define CL(a, v) memset((a), (v), sizeof(a))
#define mp make_pair
#define X first
#define Y second
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))

typedef long long ll;
typedef vector<int> VI;
typedef pair<int, int> pii;

/*** TEMPLATE CODE ENDS HERE */

int main() {
#ifdef LOCAL_HOST
  //  freopen("C-small-attempt1.in", "r", stdin);
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  assert(T == 1);
  int n, m;
  cin >> n >> m;
  cout << "Case #1:" << endl;
  ll divs[10];

  for (ll tmask = 1; tmask < (1ll << min(10, n - 2)); ++tmask) {
    ll mask = tmask << 1;
    mask |= 1;
    mask |= 1ll << (n - 1);
    int sz = 0;
    for (int base = 2; base <= 10; ++base) {
      ll m = 1;
      ll x = 0;
      rep(i, n) {
        if ((mask >> i) & 1) {
          x += m;
        }
        m *= base;
      }
      for (ll i = 2; i * i <= x; ++i) {
        if (x % i == 0) {
          divs[sz++] = i;
          break;
        }
      }
    }
    if (sz == 9) {
      for (int i = n - 1; i >= 0; --i) cout << ((mask >> i) & 1);
      rep(i, sz) cout << " " << divs[i];
      cout << endl;
      --m;
    }
    if (m == 0) {
      break;
    }
  }
  assert(m == 0);

  return 0;
}
