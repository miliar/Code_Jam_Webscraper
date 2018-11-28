#include "stdc++.h"
using namespace std;

#define DEBUG 0

int main() {
  int tc, cn, D, P[1000], mx, best, t, i, j;
  scanf("%d", &tc);
  for(cn = 1; cn <= tc; cn++) {
    scanf("%d", &D);
    for(i = 0, mx = 1; i < D; i++) {
      scanf("%d", &P[i]);
      mx = max(mx, P[i]);
    }
    best = mx;
    for(i = 1; i < mx; i++) {
      for(j = 0, t = i; j < D; j++)
	t += (P[j] + i - 1) / i - 1;
      if(DEBUG)
	printf("i = %d, t = %d\n", i, t);
      best = min(best, t);
    }
    printf("Case #%d: %d\n", cn, best);
  }
  return 0;
}
