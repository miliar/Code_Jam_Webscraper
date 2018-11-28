#define __STDC_FORMAT_MACROS
#include <stdint.h>
#include <inttypes.h>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <vector>
using namespace std;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define REP1(i, n) for (int i = 1; i <= (n); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define ROF(i, a, b) for (int i = (b); --i >= (a); )

#define iter(v) __typeof((v).begin())
#define foreach(it, v) for (iter(v) it = (v).begin(); it != (v).end(); it++)

#define PB push_back
#define MP make_pair
#define fi first
#define se second

typedef vector<int> VI;
typedef set<int> SI;
typedef pair<int, int> PII;
typedef map<int, int> MII;

typedef int64_t i64;

const int M = 3000;
const int MOD = 1000002013;

int RI()
{
  int x;
  scanf("%d", &x);
  return x;
}

i64 RL()
{
  i64 x;
  scanf("%" SCNd64, &x);
  return x;
}

//bool check(i64 x)
//{
  //i64 lo = 0, hi = 1LL << n, large = hi - 1 - x;
  //REP(i, n) {
    //if (hi <= p) return true;
    //i64 mi = (lo + hi) / 2;
    //if (large > 0) {
      //hi = mi;
    //}
    //large /= 2;
  //}
  //return hi <= p;
//}

int main()
{
  int cases = RI();
  REP1(cc, cases) {
    int n = RI();
    i64 p = RL();

    i64 y = 0, z = 0;
    for (int i = n; --i >= 0; ) {
      if (y + (1LL << i) < p) {
        y += 1LL << i;
        z += 1LL << n - i;
        z = min(z, (i64(1) << n) - 1);
      } else
        break;
    }

    i64 w = 0, x = 0;
    for (int i = 0; i < n; i++) {
      if (w + (1LL << i) < p) {
        w += 1LL << i;
        x += 1LL << n-1-i;
      } else
        break;
    }

    printf("Case #%d: %" PRId64 " %" PRId64 "\n", cc, z, x);
  }
}
