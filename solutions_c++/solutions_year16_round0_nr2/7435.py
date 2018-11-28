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
  uint64_t T;
  Input >> T;
  for (uint64_t C = 1; C <= T; C++) {
    std::string Stack;
    Input >> Stack;
    char Current = Stack[0];
    uint64_t Count = (Current == '+' ? 0 : 1);
    for (char Pancake : Stack) {
      if (Pancake == Current)
        continue;
      if (Pancake == '-')
        Count += 2;

      Current = Pancake;
    }
    if (Current == '-' && Count == 0)
      Count++;

    std::cout << "Case #" << C << ": " << Count << "\n";
  }
}
