#include <iostream>
#include <string>
#include <set>

int main() {
  int number_of_tests;
  std::cin >> number_of_tests;
  for (int test_index = 0; test_index < number_of_tests; ++test_index) {
    int n;
    std::cin >> n;
    std::cout << "Case #" << test_index + 1 << ": ";
    if (n == 0) {
      std::cout << "INSOMNIA" << std::endl;
      continue;
    }
    std::set<char> used_digits;
    for (int i = 1; i <= 100; ++i) {
      int number = i * n;
      std::string string = std::to_string(number);
      for (char ch : string) {
        used_digits.insert(ch);
      }
      if (used_digits.size() == 10) {
        std::cout << number << std::endl;
        break;
      }
    }
  }
  return 0;
}
