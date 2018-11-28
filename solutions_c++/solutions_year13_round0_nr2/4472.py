#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define REP(i, n) for(int i = 0; i < (n); ++i)
#define FOR(i, p, k) for(int i = (p); i <= (k); ++i)

int T[100][100];
int mr[100], mc[100];
int R, C;

bool kk() {
  REP(r, R) REP(c, C) {
    if (T[r][c] < min(mr[r], mc[c])) return false;
  }
  return true;
}

int main() {
  int Z; scanf("%d", &Z);
  FOR(t, 1, Z) {
    scanf("%d %d", &R, &C);
    memset(mr, 0, 100 * sizeof(int));
    memset(mc, 0, 100 * sizeof(int));
    REP(r, R) REP(c, C) {
      scanf("%d", &T[r][c]);
      mr[r] = max(mr[r], T[r][c]);
      mc[c] = max(mc[c], T[r][c]);
    }
    
    printf("Case #%d: %s\n", t, kk() ? "YES" : "NO");
  }
  return 0;
}
