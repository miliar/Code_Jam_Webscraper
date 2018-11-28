#include <stdio.h>
#include <math.h>
#include <inttypes.h>

int update_digits(const int64_t number, const int N, bool* digits) {
  for (int i = 1; i < N - 1; ++i) {
    digits[i] = (number >> i) & 1;
  }
  return 0;
}

int64_t compute_number(const bool* digits, const int N, const int base) {
  int64_t number = 1;
  for (int i = 1; i < N; ++i) {
    number += digits[i]? pow(base, i) : 0;
  }
  return number;
}

int64_t get_divisor(const int64_t number) {
  for (int64_t i = 2; i < sqrt(number); ++i) {
    if (number % i == 0) {
      return i;
    }
  }
  return 0;
}

int generate(const int N, const int J) {
  bool* digits = new bool[N]();
  digits[0] = true;
  digits[N - 1] = true;
  int num_pass = 0;
  for (int64_t i = 0; i < (1LL << (N - 2)); ++i) {
    int64_t number = (1LL << (N - 1)) + (i << 1) + 1;
    update_digits(number, N, digits);
    int pass = true;
    int64_t divisors[9] = {0};
    for (int base = 2; base <= 10; ++base) {
      number = compute_number(digits, N, base);
      divisors[base - 2] = get_divisor(number);
      if (divisors[base - 2] == 0) {
        pass = false;
        break;
      }
    }
    if (pass) {
      for (int i = N - 1; i >= 0; --i) {
        printf("%d", digits[i]);
      }
      printf(" ");
      for (int i = 0; i <= 8; ++i) {
        printf("%" PRId64" ", divisors[i]);
      }
      printf("\n");
      ++num_pass;
      if (num_pass >= J) {
        return 0;
      }
    }
  }
  delete[] digits;
  return 0;
}


int main() {
  int T = 0;
  scanf("%d", &T);
  for (int i = 0; i < T; ++i) {
    int N = 0;
    int J = 0;
    scanf("%d %d", &N, &J);
    printf("Case #%d:\n", i + 1);
    generate(N, J);
  }
  return 0;
}

