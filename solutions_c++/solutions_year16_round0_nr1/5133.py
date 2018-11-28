#include <stdio.h>

int compute(const bool* digits) {
  int num_digits_seen = 0;
  for (int i = 0; i < 10; ++i) {
    num_digits_seen += digits[i];
  }
  return num_digits_seen;
}

int solve(const int test_index, bool* digits) {
  int N = 0;
  scanf("%d", &N);
  for (int multiply = 1; multiply <= 1000; ++multiply) {
    int number = multiply * N;
    int divisor = 1;
    while (number > 0) {
      int digit = number - (number / (divisor * 10)) * 10;
      digits[digit] = true;
      if (compute(digits) == 10) {
        printf("Case #%d: %d\n", test_index, multiply * N);
        return 0;
      }
      number = (number - digit) / 10;
    }
  }
  printf("Case #%d: INSOMNIA\n", test_index);
  return 0;
}


int main() {
  int T = 0;
  scanf("%d", &T);
  for (int i = 0; i < T; ++i) {
    bool digits[10] = {false};
    solve(i + 1, digits);
  }
  return 0;
}

