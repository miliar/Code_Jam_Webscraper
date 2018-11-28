#include <cstdio>
#include <algorithm>

int main() {
  int T, smax;

  scanf("%i", &T);

  for (int t = 1; t <= T; ++t) {
    scanf("%i", &smax);
    int sum = 0, solution = 0;
    for (int i = 0; i <= smax; ++i) {
      char c;
      scanf(" %c", &c);
      solution = std::max(solution, i - sum);
      sum += c - '0';
    }
    printf("Case #%i: %i\n", t, solution);
  }

  return 0;
}
