#include <iostream>
#include <bitset>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <math.h>

long long is_prime(long long num)
{
  if (num < 2)
    return 1;

  if (num > 2 && (num % 2) == 0)
    return 2;

  long double num_d = static_cast<long double>(num);
  long long upperLimit = static_cast<long long>(sqrt(num_d) + 1);

  for(long long i = 3; i < upperLimit; i += 2)
  {
    if ((num % i) == 0)
    {
      return i;
    }
  }
  return 0;
}

bool check_jamcoin(std::string nbr) {
  std::vector<long long> v;
  char *end;
  long long divisor;
  for (unsigned int base = 2; base <= 10; base++) {
    long long result = strtoll(nbr.c_str(), &end, base);
    if ((divisor = is_prime(result)) == 0)
      return false;
    v.push_back(divisor);
  }
  std::cout << strtoll(nbr.c_str(), &end, 10);
  std::for_each(v.begin(), v.end(), [](long long elem) {
    std::cout << " " << elem;
  });
  std::cout << std::endl;
  return true;
}

void do_test_case(unsigned int T) {
  for (unsigned int i = 0; i < T; i++) {
    unsigned int N, J;

    std::cin >> N >> J;
    std::cout << "Case #" << (i + 1) << ":" << std::endl;
    unsigned int nbr = pow(2, N - 1) + 1;
    std::bitset<33> s = std::bitset<33>(nbr);
    while (s[N - 1] == 1 && J > 0) {
      if (check_jamcoin(s.to_string())) {
        J--;
      }
      nbr += 2;
      s = std::bitset<33>(nbr);
    }
  }
}

int main() {
  unsigned int T;
  std::cin >> T;
  if (T < 1 || T > 100) {
    std::cerr << "T must be a number between 1 and 100." << std::endl;
    return 1;
  }
  do_test_case(T);
  return 0;
}
