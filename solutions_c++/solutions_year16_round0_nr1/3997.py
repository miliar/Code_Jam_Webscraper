#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <assert.h>
#include <iostream>
#include <string.h>

static int32_t get_digits(int64_t n)
{
  int32_t ret = 0;
    while (n != 0) {
      int32_t d = n % 10;
        ret |= (1u << d);
        n /= 10;
    }
  return ret;
}

static int64_t get_min_steps(int64_t n)
{
  int32_t digits = 0;
  int64_t step = 0;
  int64_t m = n;
    while (digits != 0x3ff) {
        digits |= get_digits(m);
        ++step;
        m += n;
    }
  return step*n;
}

int32_t main(int32_t argc, char **argv)
{
  int64_t n, t;
    std::cin >> t;
    for (int64_t i = 1; i <= t; ++i) {
        std::cin >> n;
        if (n == 0) {
            fprintf(stdout, "Case #%ld: INSOMNIA\n", i);
        }
        else {
            fprintf(stdout, "Case #%ld: %ld\n", i, get_min_steps(n));
        }
    }
  return 0;
}
