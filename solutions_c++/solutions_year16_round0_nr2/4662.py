#include <iostream>
#include <sstream>
#include <stack>
#include <algorithm>

void do_test_case(unsigned int T) {
  for (unsigned int i = 0; i < T; i++) {
    std::string line;

    std::cin >> line;
    if (line.length() >= 1 && line.length() <= 100) {
      unsigned int count = 0;
      bool top_happy_side_up = (line[0] == '+');
      char pancake = line[0];
      for (unsigned int idx = 1, end = line.length(); idx < end; idx++) {
        if (pancake != line[idx]) {
          count++;
          top_happy_side_up = !(top_happy_side_up);
          pancake = line[idx];
        }
      }
      if (top_happy_side_up == false)
        count++;
      std::cout << "Case #" << (i + 1) << ": " << count << std::endl;
    } else {
      std::cerr << "Case #" << (i + 1) << ": Invalid S." << std::endl;
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
