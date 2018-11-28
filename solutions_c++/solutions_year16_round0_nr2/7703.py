// g++ -lm -lcrypt -O2 -std=c++11 -pipe main.cpp && ./a.out

#include <iostream>
#include <fstream>
bool verbose;

int flipit(std::string stack) {
  if(verbose)
    std::cout << stack << std::endl;
  int flips = 0;
  if (stack.empty()) return 0;
  auto last = stack[0];
  for(int i = 1; i < stack.size(); i++) {
    if (last != stack[i]) {
      flips++;
      last = stack[i];
    }
  }
  if (last == '-') flips++;
  return flips;
}


int main(int argc, char *argv[]) {
  verbose = argc > 2;
  if (argc >= 2) {
    std::ifstream ifs(argv[1]);
    int cnt;
    ifs >> cnt;
    for(int i = 0; i <= cnt; i++) {
      std::string line;
      getline(ifs, line);
      if (i == 0) continue;
      auto c = flipit(line);
      std::cout << "Case #" << (i) << ": ";
      std::cout << c << std::endl;
    }
  }
  return 0;
}
