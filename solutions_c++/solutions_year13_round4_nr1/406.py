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

struct T
{
  int e, p;
  bool operator<(const T& r) const {
    return e < r.e || e == r.e && p > r.p;
  }
} a[M], b[M];

i64 f(int x)
{
  return i64(x) * (x-1) / 2 % MOD;
}

int main()
{
  int cases = RI();
  REP1(cc, cases) {
    int n = RI(), m = RI();
    i64 ans = 0;
    REP(i, m) {
      a[i].e = RI();
      a[m+i].e = RI();
      a[i].p = RI();
      a[m+i].p = - a[i].p;
      ans -= f(a[m+i].e - a[i].e) * a[i].p;
      ans %= MOD;
    }

    int top = 0;
    sort(a, a + m * 2);
    REP(i, m * 2) {
      if (a[i].p > 0) {
        b[top++] = a[i];
      } else {
        int x = - a[i].p;
        while (x > 0) {
          int y = min(x, b[top-1].p);
          b[top-1].p -= y;
          x -= y;
          ans += f(a[i].e - b[top-1].e) * y;
          ans %= MOD;
          if (b[top-1].p == 0) top--;
        }
      }
    }

    ans = (ans % MOD + MOD) % MOD;
    printf("Case #%d: %" PRId64 "\n", cc, ans);
  }
}
