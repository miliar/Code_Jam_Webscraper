#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
#include <string>
#include <unistd.h>
#include <stdint.h>

void checkDigit(std::string& nbSeen, int nb)
{
  std::string result = std::to_string(nb);
  std::size_t found;

  for (uint64_t i = 0; i < result.size(); i++) {
    if ((found = nbSeen.find(result[i])) == std::string::npos)
      nbSeen += result[i];
  }
  std::sort(nbSeen.begin(), nbSeen.end());
}

int main() {
  std::ifstream infile("tmp.in");
  uint64_t cases = 1;
  uint64_t T;
  uint64_t N;
  uint64_t i;
  uint64_t result;
  std::string allNb = "0123456789";
  std::string nbSeen;

  infile >> T;

  while (infile >> N) {
    nbSeen.clear();

    if (N == 0) {
      std::cout << "Case #" << cases << ": INSOMNIA" << std::endl;
    }
    else {
      i = 1;
      while (allNb != nbSeen) {
        result = N * i;
        checkDigit(nbSeen, result);
        ++i;
      }
      std::cout << "Case #" << cases << ": " << result << std::endl;
    }
    ++cases;
  }

  return 0;
}
