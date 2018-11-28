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

#include "InfInt.h" /* https://github.com/sharan01/infint/blob/master/InfInt.h */

static const std::vector<InfInt> smallPrimes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 };

bool getDevisorFast(InfInt number, InfInt &divisor) {
  for (size_t i = 0; i < smallPrimes.size(); ++i) {
    if (number % smallPrimes[i] == 0) {
      divisor = smallPrimes[i];
      return true;
    }
  }
  return false; // number may be not a prime, but we skip it because it takes too long!
}

/* can be used instead of getDevisorFast with numbers who have a bigger prime than smallPrimes.size() as devisor */
/* but computing will take much longer */
bool getDevisor(InfInt number, InfInt &divisor) {
  if (number <= 3) {
    if (number > 1) {
      return false;
    }
    else {
      // 1 and 0 have no non-trivial divisor
      divisor = 0;
      return true;
    }
  }
  else if (number % 2 == 0) {
    divisor = 2;
    return true;
  }
  else if (number % 3 == 0) {
    divisor = 3;
    return true;
  } else {
    for (InfInt i = 5; i * i <= number; i += 6) {
      if (number % i == 0) {
        divisor = i;
        return true;
      }
      else if (number % (i + 2) == 0) {
        divisor = i + 2;
        return true;
      }
    }
    return false;
  }
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args(argv, argv + argc);
  args.erase(args.begin());
  if (args.size() >= 2) {
    std::ifstream input(args.at(0));
    if (input) {
      std::srand(static_cast<unsigned int>(std::time(0)));
      std::string line;
      std::vector<std::string> lines;
      std::ofstream output(args.at(1));
      while (std::getline(input, line)) {
        lines.emplace_back(line);
      }
      if (lines.size() > 0) {
        size_t totalTestcases = std::stoi(lines.at(0));
        totalTestcases = std::min(totalTestcases, (lines.size() - 1));
        std::function<bool(InfInt, InfInt&)> divisorFunction = getDevisorFast; /* try the faster function first */
        for (size_t i = 0; i < totalTestcases; i++) {
          size_t lengthOfCoin = std::stoi(lines.at(i + 1).substr(0, lines.at(i + 1).find_first_of(" ")));
          size_t numberOfResults = std::stoi(lines.at(i + 1).substr(lines.at(i + 1).find_last_of(" ")));
          std::stringstream stream;
          stream << "Case #" << (i + 1) << ":" << std::endl;
          std::vector<std::string> baseNumbers;
          std::vector<std::string> permutations;
          for (size_t i = 0; i <= lengthOfCoin - 2; ++i) {
            std::string baseNumber;
            baseNumber += std::string(i, '0');
            baseNumber += std::string(lengthOfCoin - 2 - i, '1');
            baseNumbers.emplace_back(baseNumber);
          }
          size_t resultsFound = 0;
          for (size_t i = 0; i < baseNumbers.size(); ++i) {
            std::string str = baseNumbers.at(i);
            do {
              std::string currentNumber = "1" + str + "1";
              bool noPrime = true;
              std::vector<InfInt> devisors;
              for (size_t j = 2; j <= 10; ++j) {
                InfInt numberInBaseX = 0;
                for (long long k = currentNumber.size() - 1; k >= 0; --k) {
                  InfInt power = 1;
                  for (long long l = 0; l < currentNumber.size() - (k + 1); ++l) {
                    power = power * j;
                  }
                  numberInBaseX += InfInt(currentNumber[k] - '0') * power;
                }
                InfInt devisor = 0;
                
                if (divisorFunction(numberInBaseX, devisor)) {
                  devisors.emplace_back(devisor);
                }else {
                  noPrime = false;
                  break;
                }
              }
              if (noPrime) {
                std::cout << resultsFound + 1 << "/" << numberOfResults << std::endl;
                stream << currentNumber << " ";
                for (size_t j = 0; j < devisors.size(); ++j) {
                  stream << devisors[j];
                  if (j + 1 < devisors.size()) {
                    stream << " ";
                  }
                }
                stream << std::endl;
                resultsFound++;
              }
            } while ((resultsFound < numberOfResults) && (std::next_permutation(str.begin(), str.end())));
            if (resultsFound >= numberOfResults) {
              output << stream.str();
              divisorFunction = getDevisorFast; /* for next testcase try first the faster function first */
              break;
            }
          }
          if (resultsFound < numberOfResults) {
            if (*divisorFunction.target<bool(*)(InfInt, InfInt&)>() != getDevisor) {
              i--;
              /* not enough results found -> try again the same testcase with getDevisor() instead of getDevisorFast() to find all possibilities */
              divisorFunction = getDevisor;
            }else {
              /* already tried all possibilities -> input file is not solvable */
              /* proceed to next testcase */
              divisorFunction = getDevisorFast; /* for next testcase try first the faster function first */
            }
          }
        }
      }
    }
  }
  return EXIT_SUCCESS;
}