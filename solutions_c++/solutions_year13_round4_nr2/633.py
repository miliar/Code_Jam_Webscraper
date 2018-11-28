#include <iostream>
#include <algorithm>
#include <vector>
#include <cassert>

typedef long long int lld;

lld reverse(lld v, int bits) {
  unsigned int r = 0; // r will be reversed bits of v; first get LSB of v
  for (int i=0; i<bits; ++i)
    if ( v & (1ull<<i) )
      r |= 1ull << (bits - i - 1);
  return r;
}

int main()
{
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);
  std::cin.exceptions(std::ios_base::failbit | std::ios_base::badbit);
  int testcases = 0; std::cin >> testcases;

  for (int case_nr=1; case_nr<=testcases; ++case_nr) {
    std::cout << "Case #" << case_nr << ": ";    

    lld n, p;
    std::cin >> n >> p;

    std::vector<int> vec;
    for (unsigned i=0; i<(1ull<<n); ++i)
      vec.push_back(reverse(i, n));

    if (p == 1ull<<n)
      std::cout << p-1 << ' ' << p-1;
    else
      std::cout << *std::min_element(vec.begin()+p,   vec.end())-1 << ' '
                << *std::max_element(vec.begin(), vec.begin()+p);
    
    std::cout << '\n';
  }
}

/*
 * Local variables:
 * mode:c++
 * compile-command:"rm -f fast-prices && g++ -g -ggdb3 -O0 -D_GLIBCXX_DEBUG -Wall -Wextra -pedantic -Wno-long-long -std=c++11 prices.cc -o prices && for f in *.in; do echo \"--- $f -------------\"; ./prices <$f; done && g++ -Ofast -fwhole-program -march=native -std=c++11 prices.cc -o fast-prices"
 * end:
 */
