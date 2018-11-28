#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define REP(i,n) for (int i = 1; i <= n; ++i)

int ncases;
int p[1001];

int f(int lmt)
{
  int ncuts = 0;
  REP(d,1000) {
    if (d <= lmt || p[d] == 0) continue;
    int a = d / lmt; if (a * lmt < d) a++;
    ncuts += (a - 1) * p[d];
  }
  return lmt + ncuts;
}

int solve()
{
  REP(i,1000) p[i] = 0;
  int d; scanf(" %d", &d);
  REP(i,d) {
    int c; scanf(" %d", &c);
    p[c]++;
  }

  int best_time = 1000;
  REP(lmt,1000) {
    if (best_time < lmt) break;
    best_time = min(best_time, f(lmt));
  }

  return best_time;
}

int main()
{
  scanf(" %d", &ncases);
  REP(i, ncases)
    printf("Case #%d: %d\n", i, solve());

  return 0;
}
