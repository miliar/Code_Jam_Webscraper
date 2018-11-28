#include <algorithm>
#include <iostream>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

int test_case_number_ = 0;
#define gout printf("Case #%d: ", ++test_case_number_),cout

void solution() {
  int N, J;
  cin >> N >> J;
  int gen_digits = min(14, N - 2);
  gout << endl;
  for (int mask = 0; mask < (1 << gen_digits) && J > 0; ++mask) {
    if ((__builtin_popcount(mask) + 2) % 6 != 0) {
      continue;
    }

    int sum2 = 1, i2 = 2;
    for (int i = 0; i < gen_digits; ++i) {
      if ((1 << i) & mask) {
        sum2 = sum2 + i2;
      }
      i2 = 3 - i2;
    }
    for (int i = 0; i < N - gen_digits - 2; ++i) {
      i2 = 3 - i2;
    }
    sum2 += i2;

    if (sum2 % 3 == 0) {
      --J;
      printf("1");
      for (int i = 0; i < N - gen_digits - 2; ++i) {
        printf("0");
      }
      for (int i = gen_digits-1; i >= 0; --i) {
        printf("%d", ((mask >> i) & 1));
      }
      printf("1");
      for (int i = 2; i <= 10; ++i) {
        if (i == 6) {
          printf(" 7");
        } else if (i % 2 == 0) {
          printf(" 3");
        } else {
          printf(" 2");
        }
      }
      puts("");
    }
  }
  assert(J == 0);
}

int main() {
  int test_cases;
  cin >> test_cases;
  for (int t_case = 0; t_case < test_cases; ++t_case) {
    solution();
  }

  return 0;
}
