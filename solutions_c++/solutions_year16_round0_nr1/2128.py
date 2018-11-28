#include <algorithm>
#include <stdio.h>

using namespace std;

int main() {
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    int n; scanf("%d", &n);
    int ret = 0;
    if (n != 0) {
      int ct = 0;
      bool seen[10];
      for (int i = 0; i < 10; i++) {
        seen[i] = false;
      }
      int m = 0;
      while (ct != 10) {
        m += n;
        int k = m;
        while (k != 0) {
          int d = k % 10;
          if (!seen[d]) {
            seen[d] = true;
            ct++;
          }
          k /= 10;
        }
      }
      ret = m;
    }

    printf("Case #%d: ", t);
    if (ret == 0) {
      printf("INSOMNIA\n");
    } else {
      printf("%d\n", ret);
    }
  }
}
