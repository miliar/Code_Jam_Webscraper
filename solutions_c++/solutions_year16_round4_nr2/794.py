#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>

const size_t kMaxN = 200;

double g_table[kMaxN + 1][kMaxN + 1][kMaxN + 1];

int PopCount(int mask) {
  int result = 0;
  for (; mask; mask = mask & (mask - 1))
    ++result;
  return result;
}

double Solve(int n, int k, double p[]) {
  double result = 0.0;

  for (int mask = 0; mask < (1 << n); ++mask) {
    if (PopCount(mask) != k)
      continue;

    double pt = 0.0;
    for (int sub = mask; sub != 0; sub = (sub - 1) & mask) {
      if (PopCount(sub) != k / 2)
        continue;

      double ps = 1.0;
      for (int i = 0; i < n; ++i) {
        if ((mask & (1 << i)) == 0)
          continue;
        if (sub & (1 << i))
          ps *= p[i];
        else
          ps *= (1.0 - p[i]);
      }
      pt += ps;
    }

    if (pt > result)
      result = pt;
  }

  return result;
}

int main() {
  int num_tests;
  scanf("%d", &num_tests);
  for (int test_num = 1; test_num <= num_tests; ++test_num) {
    int n, k;
    scanf("%d%d", &n, &k);
    double p[kMaxN];
    for (int i = 0; i < n; ++i)
      scanf("%lf", &p[i]);
    printf("Case #%d: %.7lf\n", test_num, Solve(n, k, p));
  }
  return 0;
}
