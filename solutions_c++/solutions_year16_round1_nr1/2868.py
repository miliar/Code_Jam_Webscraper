#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <limits>
#include <algorithm>
#include <functional>
#include <bitset>


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
          std::string word = lines.at(i + 1);
          std::string resultWord;
          for (size_t letter = 0; letter < word.size(); letter++) {
            char l = word[letter];
            if (resultWord.size() == 0) {
              resultWord += l;
            }else {
              if (resultWord[0] <= l) {
                resultWord.insert(resultWord.begin(), l);
              }
              else {
                resultWord += l;
              }
            }
          }
          output << "Case #" << (i + 1) << ": " << resultWord << std::endl;
        }
      }
    }
  }
  return EXIT_SUCCESS;
}