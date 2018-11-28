#include <cstdio>
#include <vector>

const int N = 16;
const int J = 50;

int getDivisor(long long number) {
  if (number <= 2) {
    return 1;
  }
  for (long long d = 2; d * d <= number; ++d) {
    if (number % d == 0) {
      return d;
    }
  }
  return 1;
};

int main() {
  int numOutput = 0;
  printf("Case #1:\n");
  for (int i = 0; i < (1 << (N - 2)) && numOutput < J; ++i) {
    std::vector<int> divisors;
    for (int base = 2; base <= 10; ++base) {
      long long number = 1;
      long long blah = base;
      for (int j = 0; j < N - 2; ++j) {
        number += ((i >> j) & 1) * blah;
        blah *= base;
      }
      number += blah;
      // fprintf(stderr, "base = %d, number = %lld\n", base, number);
      divisors.push_back(getDivisor(number));
      if (divisors.back() == 1) {
        goto foundPrime;
      }
    }
    ++numOutput;
    printf("1");
    for (int j = N - 3; j >= 0; --j) {
      printf("%c", '0' + ((i >> j) & 1));
    }
    printf("1");
    for (int x : divisors) {
      printf(" %d", x);
    }
    printf("\n");
foundPrime:
    continue;
  }
}
