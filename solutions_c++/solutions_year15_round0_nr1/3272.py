#include <cstdio>

const int N = 1000 + 10;

char numbers[N];

int main() {
  int test;
  scanf("%d", &test);
  for (int t = 1; t <= test; ++ t) {
    int result = 0, n = 0;
    scanf("%d%s", &n, numbers);
    for (int i = 0, sum = 0; i <= n; ++ i) {
      int x = numbers[i] - '0';
      if (x == 0) continue;
      if (sum < i) {
        result += i - sum;
        sum = i;
      }
      sum += x;
    }
    printf("Case #%d: %d\n", t, result);
  }
  return 0;
}
