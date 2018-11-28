#include <limits>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
#include <queue>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; ++i)
#define REP(i,n) for (int i = 1; i <= n; ++i)

int R, C, N;
int t[20][20];

void init()
{
  scanf(" %d %d %d", &R, &C, &N);
}

int bits(int i)
{
  int j = i;
  int cnt = 0;
  while (j) {
    if (j & 1) ++cnt;
    j >>= 1;
  }

  return cnt;
}

void set(int b)
{
  FOR (i, R + 1) FOR (j, C + 1) t[i][j] = 0;
  FOR (i, R) FOR (j, C) t[i][j] = (b  >> (i * C + j)) & 1;
}

long solve()
{
  init();

  long ans = numeric_limits<long>::max();
  int RC = R * C;
  FOR(b,1 << RC) {
    if (bits(b) != N) continue;
    set(b);

//     FOR(i, R) {
//       FOR(j, C) printf(" %d", t[i][j]);
//       puts("");
//     }
//     puts("");

    long uh = 0;
    FOR (i,R) FOR (j,C) {
      if (t[i][j] && t[i + 1][j]) uh++;
      if (t[i][j] && t[i][j + 1]) uh++;
    }
    ans = min(ans, uh);
  }

  return ans;
}

int main()
{
  int ncases;
  scanf(" %d", &ncases);
  REP(i, ncases)
    printf("Case #%d: %ld\n", i, solve());

  return 0;
}
