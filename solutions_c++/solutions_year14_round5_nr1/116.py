#include <algorithm>
#include <cstdio>
#include <stdint.h>
#include <cinttypes>
#include <cstdlib>
#include <functional>
#include <map>
#include <set>
#include <utility>
#include <vector>
using namespace std;
typedef int64_t i64;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define REP1(i, n) for (int i = 1; i <= (n); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define ROF(i, a, b) for (int i = (b); --i >= (a); )
#define pb push_back
#define mp make_pair
#define fi first
#define se second

typedef vector<int> VI;
typedef pair<int, int> PII;

int ri()
{
  int x;
  scanf("%d", &x);
  return x;
}

const int N = 1000000;
int a[N];
i64 sum[N];

int main()
{
  int cases = ri();
  REP1(cc, cases) {
    int n = ri(), p = ri(), q = ri(), r = ri(), s = ri();
    REP(i, n) {
      a[i] = (i*p+q)%r+s;
      sum[i] = a[i];
      if (i) sum[i] += sum[i-1];
    }
    i64 l = (sum[n-1]+2)/3, ans = sum[n-1];
    r = sum[n-1];
    while (l < r) {
      i64 m = (l+r) >> 1;
      int x = upper_bound(sum, sum+n, m) - sum;
      int y = upper_bound(sum+x, sum+n, m+(x?sum[x-1]:0)) - sum;
      if (sum[n-1]-(y?sum[y-1]:0) <= m) {
        ans = min(ans, m);
        r = m;
      } else
        l = m+1;
    }
    printf("Case #%d: %.10lf\n", cc, double(sum[n-1]-l)/sum[n-1]);
  }
}
