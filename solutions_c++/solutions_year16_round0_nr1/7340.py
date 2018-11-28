#include <cstdint>
#include <fstream>
#include <iostream>

void solve(std::istream &Input);

int main(int argc, const char **argv) {
  if (argc == 2) {
    std::fstream Input(argv[1]);
    solve(Input);
  } else if (argc == 1) {
    solve(std::cin);
  } else {
    std::cout << "Usage: " << argv[0] << " [InputFile]\n";
  }
}

void solve(std::istream &Input) {
  uint64_t T, N;

  Input >> T;
  for (uint64_t C = 1; C <= T; C++) {
    Input >> N;
    if (N == 0) {
      std::cout << "Case #" << C << ": INSOMNIA\n";
      continue;
    }

    bool SeenDigits[10] = {false, false, false, false, false,
                           false, false, false, false, false};
    uint64_t missing = 10;
    uint64_t number = 0;
    while (missing > 0) {
      number += N;
      uint64_t rem = number;
      while (rem > 0) {
        uint64_t d = rem % 10;
        if (!SeenDigits[d])
          missing--;
        SeenDigits[d] = true;
        rem /= 10;
      }
    }
    std::cout << "Case #" << C << ": " << number << "\n";
  }
}
