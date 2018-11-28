#include <iostream>
#include <string>

int main() {
  int number_of_tests;
  std::cin >> number_of_tests;

  std::string temp;
  std::getline(std::cin, temp);

  for (int test_index = 0; test_index < number_of_tests; ++test_index) {
    std::string string;
    std::getline(std::cin, string);
    int number_of_changes = 0;
    for (int i = 1; i < string.length(); ++i) {
      number_of_changes += (string[i] != string[i - 1]);
    }
    if (string.back() == '-') {
      number_of_changes++;
    }
    std::cout << "Case #" << test_index + 1 << ": " << number_of_changes <<
      std::endl;
  }

  return 0;
}
