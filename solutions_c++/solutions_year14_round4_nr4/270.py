#ifdef _MSC_VER
typedef __int32 int32_t;
typedef unsigned __int32 uint32_t;
typedef __int64 int64_t;
typedef unsigned __int64 uint64_t;
#define PRId64 "I64d"
#define SCNd64 PRId64
#else
#define __STDC_FORMAT_MACROS
#include <inttypes.h>
#include <stdint.h>
#endif
#include <algorithm>
#include <climits>
#include <cstdio>
#include <functional>
#include <map>
#include <set>
#include <utility>
#include <cstring>
#include <queue>
#include <vector>
using namespace std;
typedef int64_t i64;
typedef unsigned u;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define REP1(i, n) for (int i = 1; i <= (n); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define ROF(i, a, b) for (int i = (b); --i >= (a); )
#define pb push_back
#define mp make_pair
#define fi first
#define se second
typedef double ft;

typedef vector<int> VI;
typedef pair<int, int> PII;

int ri()
{
  int x;
  scanf("%d", &x);
  return x;
}

double rd()
{
  double x;
  scanf("%lf", &x);
  return x;
}

i64 rl()
{
  i64 x;
  scanf("%" SCNd64, &x);
  return x;
}

const int M = 10, N = 5, L = 100;
struct A {
  char a[L+1];
  int l;
  bool operator<(const A &o) const {
    return strcmp(a, o.a) < 0;
  }
} a[M];
int b[M+1], lcp[M][M];

int main()
{
  int cases = ri();
  REP1(cc, cases) {
    int m = ri(), n = ri();
    REP(i, m) {
      scanf("%s", a[i].a);
      a[i].l = strlen(a[i].a);
    }
    sort(a, a+m);
    REP(i, m)
      FOR(j, i+1, m) {
        int x = 0;
        while (a[i].a[x] == a[j].a[x] && a[i].a[x])
          x++;
        lcp[i][j] = x;
      }

    int last[N], opt = 0, optc = 0;
    fill_n(b, m, 0);
    for(;;) {
      int num = n;
      fill_n(last, n, -1);
      REP(i, m) {
        if (last[b[i]] == -1)
          num += a[i].l;
        else
          num += a[i].l - lcp[last[b[i]]][i];
        last[b[i]] = i;
      }
      if (find(last, last+n, -1) == last+n) {
        if (num > opt)
          opt = num, optc = 0;
        if (num == opt)
          optc++;
      }

      int i;
      for (i = 0; ++b[i] >= n; b[i++] = 0);
      if (i >= m) break;
    }
    printf("Case #%d: %d %d\n", cc, opt, optc);
  }
}
