#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <sstream>
#include <limits>
#include <string>
#include <bitset>
#include <map>

using namespace boost::multiprecision;

uint128_t divisor(uint128_t n) {
  if(n <= 3) {
    return n;
  } else if(n%2 == 0) {
    return 2;
  } else if (n%3 == 0) {
    return 3;
  } else {
    uint128_t u;
    unsigned int it = 0;

    for(u = 5; u*u < n; u += 6) {
      if(n%u == 0) {
        return u;
      } else if(n%(u+2) == 0) {
        return u+2;
      }

      if(++it == 500) {
        break;
      }
    }

    return n;
  }
}

uint128_t getnum(unsigned int u, unsigned int base) {
  uint128_t num = 0, v = 1;
  while(u > 0) {
    if(u%2) {
      num += v;
    }
    u >>= 1;
    v *= base;
  }

  return num;
}

void coins(unsigned int N, unsigned int J) {
  unsigned int u, v, num;

  num = (1 << (N - 1)) + 1;
  while(J > 0) {
    std::stringstream ss;

    std::bitset<std::numeric_limits<unsigned int>::digits> bits(num);
    std::string str_bits = bits.to_string();
    size_t first_digit = str_bits.find('1');

    ss << str_bits.substr(first_digit);

    for(v = 2; v <= 10; ++v) {
      uint128_t p = getnum(num, v);
      uint128_t d = divisor(p);
      if(d != p) {
        ss << ' ' << d;
      } else {
        goto prime;
      }
    }

    std::cout << ss.str() << std::endl;
    --J;

    prime:
    num += 2;
  }
}

int main(int argc, char **argv) {
  unsigned int T, N, J, u;

  std::cin >> T;

  for(u = 1; u <= T; ++u) {
    std::cout << "Case #" << u << ":" << std::endl;
    std::cin >> N >> J;
    coins(N, J);
  }

  return 0;
}
