#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

typedef unsigned int uint;

bool isVowel(char c) {
  if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
    return true;
  return false;
}

int main (int argc, const char **argv) {
  unsigned int noCases;

  if (argc != 2) {
    std::cout << "syntax: exe file" << std::endl;
    return 1;
  }

  std::ifstream input;
  input.open(argv[1]);
  if (!input.is_open()) {
    std::cout << "file not found" << std::endl;
    return 1;
  }

  std::string line;
  getline(input, line);
  std::stringstream ss(line);

  ss >> noCases;

  if (noCases > 100) {
    std::cout << "T exceeds 100" << std::endl;
  }

  std::ofstream output;
  output.open("result.txt");

  for (uint i = 1;i<=noCases;i++) {
    output << "Case #" << i << ": ";
    std::cout << "Case #" << i << ": ";
    __int64 n;
    getline(input, line);
    ss = std::stringstream(line);
    std::string str;
    ss >> str >> n;

    std::vector<uint> l;

    for (unsigned int i = 0;i<str.length() - n + 1;i++) {
      bool con = true;
      for (uint j = i;j<n+i;j++) {
        if (isVowel(str[j])) {
          con = false;
          break;
        }
      }
      if (con) {
        l.push_back(i);
      }
    }

    uint sum = 0;

    for (uint i = 0;i<str.length() - n + 1;i++) {
      for (uint j = str.length();j>=n;j--) {
        uint k = 0;
        while (k < l.size() && l[k] < i) k++;
        if (k < l.size() && l[k] + n <= j) {
          sum++;
        }

      }
    }
    output << sum << std::endl;
    std::cout << sum << std::endl;

    // skip the empty line
    //getline(input, line);
  }

  input.close();
  output.close();

  return 0;
}