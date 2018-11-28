#include <iostream>
#include <string>
#include <cassert>

int main() {
  unsigned T; std::cin >> T;
  for (unsigned i1 = 1; i1 <= T; ++i1) {
    unsigned Smax; std::cin >> Smax;
    std::string s; std::cin >> s;
    assert(s.size() == 1 + Smax);
    unsigned sum = 0, result = 0;
    for (unsigned i2 = 0; i2 <= Smax; ++i2) {
      if (result < i2) {
        result = i2;
      }
      result += (unsigned)(s[i2] - '0');
      sum += (unsigned)(s[i2] - '0');
    }
    
    std::cout << "Case #" << i1 << ": " << (result - sum) << std::endl;
  }

  return 0;
}
