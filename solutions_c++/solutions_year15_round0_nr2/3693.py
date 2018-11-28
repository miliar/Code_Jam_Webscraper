#include <stdio.h>

int P[1005];

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    int D;
    scanf("%d", &D);

    for (int i = 0; i < D; i++) {
      scanf("%d", &P[i]);
    }

    int ans = 2000;
    for (int i = 1; i <= 1000; i++) {
      int cur = i;
      for (int j = 0; j < D; j++) {
        cur += (P[j] + (i-1))/i - 1;
      }

      if (cur < ans) {
        ans = cur;
      }
    }

    printf("Case #%d: %d\n", t, ans);
  }

  return 0;
}
