#include <cstdio>

int main() {
  int n,t;
  scanf("%d", &t);
  for (int ti = 1; ti <= t; ++ti) {
    scanf("%d", &n);
    
    char c;
    int x, res = 0, sum = 0;
    for (int i = 0; i <= n; ++i) {
      scanf(" %c", &c);
      x = int(c) - '0';
      if (sum < i) {
        res += (i - sum);
        sum = i;
      }
      sum += x;
    }

    printf("Case #%d: %d\n", ti, res);
  }
}
