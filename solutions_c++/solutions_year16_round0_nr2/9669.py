#include <iostream>
#include <string>

int main(int argc, char const *argv[]) {
  unsigned t;

  std::cin >> t;
  for (unsigned i = 1; i <= t; ++i) {
    unsigned flips, happy, blank;
    char last = 'x';
    std::string stack;

    std::cin >> stack;
    happy = blank = 0;
    stack.length();

    // Count the number of sets (contiguous pancakes with same side)
    for (char c : stack) {
      if (c != last) {
        if (c == '+') {
          happy++;
        } else if (c == '-') {
          blank++;
        } else {
          std::cerr << "ERROR: invalid stack character" << std::endl;
        }
      }
      last = c;
    }

    // When bottom is '+', we do one less flip
    if (stack.back() == '+')
      flips = happy + blank - 1;
    else
      flips = happy + blank;

    std::cout << "Case #" << i << ": " << flips << std::endl;
  }

  return 0;
}
