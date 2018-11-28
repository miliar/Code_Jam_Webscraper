#include <stdio.h>

int main(int argc, char *argv[]) {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    int s;
    scanf("%d", &s);
    int friends = 0;
    int sum;
    scanf("%1d", &sum);
    for (int j = 1; j <= s; j++) {
      int k;
      scanf("%1d", &k);
      if (k > 0) {
        int d = j - sum;
        if (d > 0) {
          friends += d;
          sum += d;
        }
        sum += k;
      }
    }
    printf("Case #%d: %d\n", i, friends);
  }
  return 0;
}
