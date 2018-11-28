#include <iostream>
#include <string>

int main() {
  int number_of_tests;
  std::cin >> number_of_tests;
  for (int test_index = 0; test_index < number_of_tests; ++test_index) {
    std::cout << "Case #" << test_index + 1 << ":" << std::endl;
    int n, j_in;
    std::cin >> n >> j_in;
    int found = 0;
    for (int i1 = 1; i1 + 1 < n; i1 += 2) {
      for (int j1 = 1; j1 + 1 < i1; j1 += 2) {
        for (int i2 = 2; i2 + 1 < n; i2 += 2) {
          for (int j2 = 2; j2 + 1 < i2; j2 += 2) {
            std::string result(n, '0');
            result[0] = result[n - 1] = '1';
            result[i1] = result[i2] = '1';
            result[j1] = result[j2] = '1';
            std::cout << result << ' ';
            for (int i = 2; i <= 10; ++i) {
              std::cout << i + 1;
              if (i == 10) {
                std::cout << std::endl;
              } else {
                std::cout << ' ';
              }
            }
            found++;
            if (found == j_in) {
              i1 = i2 = j1 = j2 = n;
              break;
            }
          }
        }
      }
    }
  }
  return 0;
}
