#include <iostream>

int do_test_cases(unsigned int T) {
  for (unsigned int i = 0; i < T; i++) {
    std::string line;
    std::string result;

    std::cin >> line;
    std::cout << "Case #" << (i + 1) << ": ";
    char c = line[0];
    for (unsigned int j = 0; j < line.length(); j++) {
      if (c < line[j]) {
        c = line[j];
      }
      if (c == line[j]) {
        result = c + result;
      } else {
        result += line[j];
      }
    }
    std::cout << result << std::endl;
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
  return do_test_cases(T);
}
