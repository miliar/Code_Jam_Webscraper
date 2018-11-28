#include <cstdio>
#include <cassert>

#include <iostream>
#include <algorithm>
using namespace std;

#define TRACE(x) cerr << #x << " = " << (x) << endl
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define SZ(c) ((int) (c).size())

typedef long long llint;

int main() {
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    int ans = (1 << 16) - 1;

    REP(step, 2) {
      int r;
      scanf("%d", &r); --r;

      int mask = 0;

      REP(i, 4) REP(j, 4) {
        int x;
        scanf("%d", &x); --x;
        if (i == r) mask |= 1 << x;
      }

      ans &= mask;
    }

    printf("Case #%d: ", tt);

    if (ans == 0) puts("Volunteer cheated!");
    else if ((ans & -ans) != ans) puts("Bad magician!");
    else REP(i, 16) if ((ans >> i) & 1) printf("%d\n", i+1);
  }
  return 0;
}
