#include <algorithm>
#include <cstdio>

#define MAX_N 10000

using namespace std;

int s[MAX_N];

int solve_problem(int num_case)
{
  int n, x;

  if (scanf("%d %d", &n, &x) != 2) {
    return 1;
  }

  for (int i = 0; i < n; i++) {
    if (scanf("%d", &s[i]) != 1) {
      return 1;
    }
  }

  sort(s, s + n);

  int result = 0;
  int left = 0, right = n - 1;
  for (; left < right; left++) {
    while (left < right && s[left] + s[right] > x) {
      --right;
    }
    if (left < right) {
      ++result;
      --right;
    }
  }

  printf("Case #%d: %d\n", num_case, n - result);

  return 0;
}

int main()
{
  int num_tests;

  if (scanf("%d", &num_tests) != 1) {
    return 1;
  }
  for (int i = 0; i < num_tests; i++) {
    int ret = solve_problem(i + 1);
    if (ret != 0) {
      return ret;
    }
  }

  return 0;
}
