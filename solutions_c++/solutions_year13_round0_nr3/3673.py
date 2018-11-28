#include <cmath>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

bool palindrome(size_t number)
{
  std::ostringstream oss;
  oss << number;
  const auto str = oss.str();
  const auto back = str.size() - 1;
  for(size_t i = 0; i < str.size()/2; ++i) {
    if (str[i] != str[back-i]) {
      return false;
    }
  }
  return true;
}

bool fair_and_square(size_t number)
{
  size_t root = sqrt(number);
  return (root * root == number) && palindrome(root) && palindrome(number);
}

int main(int argc, char *argv[]) {
  std::ifstream fin(argv[1]);
  size_t count;
  fin >> count;
  for(size_t i = 1; i <= count; ++i) {
    size_t lb, ub;
    fin >> lb >> ub;
    size_t count = 0;
    for(size_t j = lb; j <= ub; ++j) {
      if (fair_and_square(j)) {
        // std::cerr << "fair: " << j << std::endl;
        count++;
      }
    }
    std::cout << "Case #" << i << ": " << count << std::endl;
  }
}
