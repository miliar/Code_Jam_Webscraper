#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

unsigned int check_digits(unsigned int N) {
  std::vector<unsigned int> v;
  unsigned int i = 0;
  unsigned int result, tmp, digit;
  while (v.size() != 10) {
    result = N * i;
    tmp = result;
    while (tmp != 0 && v.size() != 10) {
      digit = tmp % 10;
      if (std::find(v.begin(), v.end(), digit) == v.end()) {
        v.push_back(digit);
      }
      tmp /= 10;
    }
    i++;
  }
  return result;
}

int do_test_case(unsigned int T) {
  unsigned int N, result = 0;
  for (unsigned int i = 0; i < T; i++) {
    std::stringstream convert;
    std::string line;

    std::cin >> line;
    convert << line;
    if (convert >> N && N <= 1000000) {
      if (N != 0) {
        result = check_digits(N);
      }
      if (result == 0 || N == 0) {
        std::cout << "Case #" << static_cast<unsigned int>(i + 1) << ": " << "INSOMNIA" << std::endl;
      } else {
        std::cout << "Case #" << static_cast<unsigned int>(i + 1) << ": " << result << std::endl;
      }
    } else {
      std::cerr << "Case #" << static_cast<unsigned int>(i + 1) << ": N is invalid." << std::endl;
    }
  }
  return 0;
}

int main() {
  unsigned int T;
  std::cin >> T;
  if (T < 1 || T > 100) {
    std::cerr << "T must be a number between 1 and 100." << std::endl;
    return 1;
  }
  return do_test_case(T);
}
