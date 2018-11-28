#include <iostream>
#include <algorithm>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp> // available at boost.org

using boost::multiprecision::cpp_int;

typedef std::vector<cpp_int> Divisors;

Divisors validateJamcoin(int n, unsigned long long coin)
{
  Divisors divisors;

  for (int base = 2; base <= 10; ++base) {
    cpp_int num = 0;

    cpp_int p = 1;
    for (int k = 0; k < n; ++k) {
      if (coin & (1 << k)) {
	num += p;
      }
      p *= base;
    }

    bool found = false;
    for (cpp_int div = 2; div <= std::min(num, cpp_int(99)); ++div) { // we only check for small divisors (and move on if there aren't any below 100)
      if (num % div == 0) {
	divisors.push_back(div);
	found = true;
	break;
      }
    }

    if (!found) {
      return Divisors();
    }
  }

  return divisors;
}

void generateJamcoins(int n, int j)
{
  int found = 0;
  
  for (unsigned long long i = 0; i < (1 << (n - 2)); ++i) {
    const unsigned long long coin = (1 << (n - 1)) | (i << 1) | 0x1;
    const Divisors divisors = validateJamcoin(n, coin);
    if (divisors.size() < 9) {
      continue;
    }

    for (int k = n - 1; k >= 0; --k) {
      std::cout << bool(coin & (1 << k));
    }
    for (int k = 0; k < divisors.size(); ++k) {
      std::cout << ' ' << divisors[k];
    }
    std::cout << std::endl;

    if (++found >= j) {
      break;
    }
  }
}

int main()
{
  int cases = 0;
  std::cin >> cases;

  for (int i = 1; i <= cases; ++i) {
    int n = 0;
    int j = 0;

    std::cin >> n >> j;
    
    std::cout << "Case #" << i << ':' << std::endl;
    generateJamcoins(n, j);
  }
  
  return 0;
}
