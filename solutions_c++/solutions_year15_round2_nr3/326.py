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

const int HTotMax = 1000;
int N;
int HTot;
int d[HTotMax];
int m[HTotMax];

void init()
{
  scanf(" %d", &N);
  HTot = 0;
  FOR (i,N) {
    int dd, hh, mm;
    scanf(" %d %d %d", &dd, &hh, &mm);
    FOR (j, hh) {
      d[HTot] = dd;
      m[HTot] = mm + j;
      ++HTot;
    }
  }
}

int solve()
{
  init();

  if (HTot <= 1) return 0;
  if (HTot == 2) {
    if (m[0] > m[1]) {
      swap(d[0], d[1]);
      swap(m[0], m[1]);
    }

    double a = m[0] * ((360 + (360 - d[0])) / 360.);
    double b = m[1] * ((360 - d[1]) / 360.);

    return a <= b;
  }

  return 0;
}

int main()
{
  int ncases;
  scanf(" %d", &ncases);
  REP(i, ncases)
    printf("Case #%d: %d\n", i, solve());

  return 0;
}
