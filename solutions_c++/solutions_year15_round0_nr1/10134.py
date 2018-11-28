#include <cstdio>

using namespace std;

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    int smax, n;
    scanf("%d %d", &smax, &n);

    int digits[smax + 1];

    int tmp = n;

    for (int i = smax; i >= 0; i--) {
      digits[i] = tmp % 10;
      tmp /= 10;
    }

    int stood = 0, cnt = 0;

    for (int i = 0; i <= smax; i++) {
      if (digits[i] == 0)
        continue;

      if (i > stood) {
	cnt += i - stood;
        stood += i - stood + digits[i];
      } else {
        stood += digits[i];
      }
    }

    printf("Case #%d: %d\n", t, cnt);
  }

  return 0;
}
