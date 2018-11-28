#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <assert.h>
#include <vector>
#include <set>
#include <iostream>

using PrimesSetT = std::set<int64_t>;

static int64_t get_divisor(const int64_t n, const int32_t b, const PrimesSetT &sp)
{
  int64_t nb = 1;
  int64_t pb = b;
    for (int32_t i = 1; i < 32; ++i) {
        if ((n & (1LL << i)) != 0) {
            nb += pb;
        }
        pb *= b;
    }

#if DEBUG > 1
    fprintf(stdout, "n = %ld; n(%d) = %ld\n", n, b, nb);
#endif // DEBUG > 1

    if (sp.count(nb) != 0) {
      return -1;
    }

    for (auto &p : sp) {
        if ((nb % p) == 0) {
          return p;
        }
    }
  return -1;
}

static void print_solutions(const int32_t n, const int32_t j, const PrimesSetT &sp)
{
  constexpr int32_t maxb = 11;
  int64_t divisors[maxb];
  int32_t count = 0;

    for (int64_t i = ((1LL << (n-1)) | 1LL); i < (1LL << n); i += 2) {
      bool prime_p = false;
      int64_t div;
        for (int32_t b = 2; b < maxb; ++b) {
            if ((div = get_divisor(i, b, sp)) == -1) {
                prime_p = true;
              break;
            }
            divisors[b] = div;
        }

        if (!prime_p) {
            fprintf(stdout, "\n");
            for (int32_t j = n-1; j >= 0; --j) {
                fprintf(stdout, "%d", (i & (1LL << j)) != 0 ? 1 : 0);
            }
            for (int32_t j = 2; j < maxb; ++j) {
                fprintf(stdout, " %ld", divisors[j]);
            }
            ++count;
        }
        if (count == j) {
          return;
        }
    }
}

int32_t main(int32_t argc, char **argv)
{
  PrimesSetT sp;
  FILE *f = fopen("c_sieve.txt", "r");
    while (!feof(f)) {
      int64_t p;
        fscanf(f, "%ld", &p);
        sp.insert(p);
    }
  fclose(f);

  int32_t t;
  int32_t n, j;
    std::cin >> t >> n >> j;
    for (int32_t i = 1; i <= t; ++i) {
        fprintf(stdout, "Case #%d: ", i);
        print_solutions(n, j, sp);
        fprintf(stdout, "\n");
    }
  return 0;
}
