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
          size_t number = std::stoi(lines.at(i + 1));
          std::string result = "INSOMNIA";
          std::set<size_t> numbers;
          if (number != 0) {
            for (size_t i = 1; i < std::numeric_limits<std::size_t>::max(); ++i) {
              size_t currentNumber = number * i;
              size_t currentNumberTemp = currentNumber;
              do {
                size_t digit = currentNumberTemp % 10;
                numbers.insert(digit);
                currentNumberTemp /= 10;
              } while (currentNumberTemp > 0);
              if (numbers.size() >= 10) {
                result = std::to_string(currentNumber);
                break;
              }
            }
          }
          
          output << "Case #" << (i + 1) << ": " << result << std::endl;
        }
      }
    }
  }
  return EXIT_SUCCESS;
}