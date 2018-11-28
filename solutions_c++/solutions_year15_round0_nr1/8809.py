#include <bits/stdc++.h>

using namespace std;

int main (void) {
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; t++) {
    int extra = 0;
    int n, cur, sum = 0;
    scanf("%d ", &n);
    for (int i = 0; i <= n; i++) {
      scanf("%1d", &cur);
      if (i > sum && cur) {
	extra += (i-sum);
	sum += (i-sum);
      }
      sum += cur;
    }
    printf("Case #%d: %d\n", t+1, extra);
  }
  return 0;
}
