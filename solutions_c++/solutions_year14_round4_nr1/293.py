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
typedef pair<int, ft> PID;
typedef pair<char, int> PCI;

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

const int N = 100000;
int a[N];

int main()
{
  int cases = ri();
  REP1(cc, cases) {
    int n = ri(), s = ri(), c = 0;
    REP(i, n)
      a[i] = ri();
    sort(a, a+n);
    for (int i = 0, j = n; i < j; j--) {
      if (i+1 < j && a[i]+a[j-1] <= s)
        i++;
      c++;
    }
    printf("Case #%d: %d\n", cc, c);
  }
}
