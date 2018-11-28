#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <limits>
#include <algorithm>

int main(int argc, char* argv[]) {
  std::vector<std::string> args(argv, argv + argc);
  args.erase(args.begin());
  if (args.size() >= 2) {
    std::ifstream input(args.at(0));
    if (input) {
      std::string line;
      std::vector<std::string> lines;
      std::ofstream output(args.at(1));
      while (std::getline(input, line)) {
        lines.emplace_back(line);
      }
      if (lines.size() > 0) {
        size_t totalTestcases = std::stoi(lines.at(0));
        totalTestcases = std::min(totalTestcases, (lines.size() - 1));
        for (size_t i = 0; i < totalTestcases; i++) {
          std::string states = lines.at(i + 1);
          size_t result = 0;
          std::vector<bool> pancakes;
          for (size_t i = 0; i < states.size();++i) {
            if (states[i] == '+') {
              pancakes.emplace_back(true);
            }else if (states[i] == '-') {
              pancakes.emplace_back(false);
            }else {
              // ignore
            }
          }
          std::reverse(pancakes.begin(), pancakes.end());
          bool currentSide = true;
          while (!pancakes.empty()) {
            size_t pancakesToRemove = 0;
            for (size_t i = 0; i < pancakes.size(); ++i) {
              if (pancakes[i] == currentSide) {
                pancakesToRemove = i + 1;
              } else {
                break;
              }
            }
            pancakes.erase(pancakes.begin(), pancakes.begin() + pancakesToRemove);
            if (!pancakes.empty()) {
              currentSide = !currentSide;
              result++;
            }
          }
          
          output << "Case #" << (i + 1) << ": " << result << std::endl;
        }
      }
    }
  }
  return EXIT_SUCCESS;
}