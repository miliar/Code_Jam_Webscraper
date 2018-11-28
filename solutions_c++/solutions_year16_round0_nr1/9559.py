#include <iostream>

int main(int argc, char const *argv[]) {
  unsigned t;

  std::cin >> t;
  for (unsigned i = 1; i <= t; ++i) {
    unsigned n, y;
    bool d[10];

    std::cin >> n;

    // If we start with 0, we'll get insomnia
    if (n == 0) {
      std::cout << "Case #" << i << ": INSOMNIA" << std::endl;
      continue;
    }

    // Clear digits vector
    for (unsigned j = 0; j < 10; ++j)
      d[j] = false;

    // Run until we find the last number
    y = 0;
    do {
      y += n;

      // Update digits
      unsigned x = y;
      while (x != 0) {
        unsigned cur = x % 10;
        x /= 10;
        d[cur] = true;
      }

    } while (!(d[0] && d[1] && d[2] && d[3] && d[4] && d[5] && d[6] && d[7] &&
               d[8] && d[9]));

    std::cout << "Case #" << i << ": " << y << std::endl;
  }

  return 0;
}
