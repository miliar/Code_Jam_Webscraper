#include <array>
#include <iostream>
#include "gcj.h"
#include <gsl.h>
#include <range/v3/algorithm/any_of.hpp>

using namespace std;
namespace rng = ranges::v3;

auto is_zero = [](auto&& d) { return d == 0; };

void count_digits(long long N, gsl::span<int,10> digits)
{
   while (N > 0) {
      ++digits[N%10];
      N /= 10;
   }
}

bool product_does_not_overflow(int i, long long N)
{
   long long max = numeric_limits<long long>::max();
   return N > 0 && N < max/i;
}

long long count_sheep(long long N)
{
   Expects(N != 0);
   array<int,10> digits {};
   int i;
   for (i = 1; rng::any_of(digits, is_zero); ++i) {
      Expects(product_does_not_overflow(i, N));
      count_digits(i*N, gsl::as_span(digits));
   }
   return (i-1)*N;
}

int main()
{
   for (int test : gcj::test_cases(cin)) {
      long long N;
      cin >> N;
      cout << "Case #" << test << ": ";
      if (N == 0)
         cout << "INSOMNIA" << '\n';
      else
         cout << count_sheep(N) << '\n';
   }
}
