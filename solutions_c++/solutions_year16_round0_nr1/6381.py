#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    int n;
    int crt = 0;
    vector<bool> digit(10, false);
    int remain = 10;
    scanf("%d", &n);
    // n = t;  // debug
    if (n == 0) {
      printf("Case #%d: INSOMNIA\n", t);
      continue;
    }
    for (int i = 0; i < 1000; i++) {
      crt += n;
      int tmp = crt;
      do {
        if (digit[tmp % 10] == false) {
          digit[tmp % 10] = true;
          remain--;
        }
        tmp /= 10;
      } while (tmp > 0);
      if (remain == 0) {
        break;
      }
      if (i == 999) {
        printf("Fail\n");
      }
    }
    if (remain > 0) {
      printf("Case #%d: INSOMNIA\n", t);
    } else {
      printf("Case #%d: %d\n", t, crt);
    }
  }
  return 0;
}
