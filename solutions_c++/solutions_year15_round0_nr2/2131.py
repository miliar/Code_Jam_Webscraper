#include <math.h>
#include <stdio.h>
#include <algorithm>

int pancakes[1002];

int main() {
  int t, n;
  scanf("%d", &t);
  for (int c = 1; c <= t; ++c) {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
      scanf("%d", &pancakes[i]);
      
    int best = 1 << 30;
    for (int i = 1; i <= 1000; ++i) {
      int specials = 0;
      for (int j = 0; j < n; ++j)
        specials += ceil((double) pancakes[j] / i) - 1;
      best = std::min(i + specials, best);
    }
    printf("Case #%d: %d\n", c, best);
  }
  return 0;
}