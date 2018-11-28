#include <stdio.h>

int main() {
  int T;
  scanf("%d", &T);

  for (int i = 1; i <= T; i++) {
    printf("Case #%d: ", i);

    unsigned long long N;
    scanf("%llu", &N);

    bool c[10];
    for (int j = 0; j < 10; ++j) {
      c[j] = false;
    }

    if (N == 0) {
      printf("INSOMNIA\n");
    } else {
      int count = 2;
      unsigned long long ans = N;
      while (1) {
        unsigned long long t = ans;
        while (t > 0) {
          int r = t % 10;
          t /= 10;
          c[r] = true;
        }
        bool flag = true;
        for (int j = 0; j < 10; ++j) {
          if (c[j] == false) {
            flag = false;
            break;
          }
        }
        if (flag == true) {
          printf("%llu\n", ans);
          break;
        }
        ans = N * count;
        ++count;
      }
    }
  }

  return 0;
}
