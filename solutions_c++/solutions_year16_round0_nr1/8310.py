#include <cstdio>
#include <cstdint>
#include <vector>

void collect_digits(std::vector<uint32_t> &digits, uint64_t num) {
  if (num > 9) {
    collect_digits(digits, num / 10);
  }
  digits.push_back(num % 10);
}

int main() {
  // 1 <= T <= 100
  uint32_t T;
  // 0 <= N <= 10^6 
  uint32_t N;

  scanf("%u", &T);

  for (size_t t = 0; t < T; ++t) {
    std::vector<bool> digits_seen;
    digits_seen.reserve(10);
    for (size_t i = 0; i < 10; ++i) digits_seen.push_back(false);

    scanf("%u", &N);
    bool found_all_digits = false;
    bool insomnia = false;
    uint32_t factor = 1;

    uint32_t multiplied_N = N;
    uint32_t previous_multiplied_N = 0;

    while (!found_all_digits) {
      found_all_digits = true;
      std::vector<uint32_t> digits;
      collect_digits(digits, multiplied_N);

      for (size_t i = 0; i < digits.size(); ++i) {
        digits_seen[digits[i]] = true;
      }

      for (size_t i = 0; i < digits_seen.size(); ++i) {
        if (digits_seen[i] == false) found_all_digits = false;
      }

      previous_multiplied_N = multiplied_N;
      multiplied_N = N * ++factor;

      if (previous_multiplied_N == multiplied_N) {
        found_all_digits = true;
        insomnia = true;
      }
    }
    printf("Case #%d: ", (t + 1));
    if (insomnia) {
      printf("INSOMNIA\n");
    }
    else {
      printf("%d\n", previous_multiplied_N);
    }
  }
  return 0;
}
