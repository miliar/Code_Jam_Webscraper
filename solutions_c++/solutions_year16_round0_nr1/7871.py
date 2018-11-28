#include <iostream>
#include <string>
#include <vector>

int main() {

  int n;
  std::cin >> n;

  for (int i = 0; i < n; ++i) {
    int number;
    std::cin >> number;

    if (number == 0) {
      std::cout << "Case #" << i+1 << ": INSOMNIA" << std::endl;
    } else {
      std::vector<char> digits = {'0','1','2','3','4','5','6','7','8','9'};
      int m = 1;
      while (digits.size() > 0) {
        std::string str = std::to_string(number*m);
        for (int j = 0; j < str.size(); ++j) {
          auto d = std::find(digits.begin(), digits.end(), str[j]);
          if (d != digits.end()) {
            digits.erase(d);
          }
        }
        m++;
      }
      std::cout << "Case #" << i+1 << ": " << (m-1)*number << std::endl;
    }
  }

  return 0;
}
