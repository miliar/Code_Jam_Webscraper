
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int solveRepeater(const vector<string>& strings) {
  const int n = strings.size();

  vector<int> pos;
  for(int i = 0; i < n; i++) {
    pos.push_back(0);
  }

  int score = 0;

  while(pos[0] < strings[0].size()) {
    char c = strings[0][pos[0]];

    int maxOcc = 0;
    int minOcc = INT_MAX;

    for(int i = 0; i < n; i++) {
      int occ = 0;

      while(pos[i] < strings[i].size() && strings[i][pos[i]] == c) {
        occ++;
        pos[i]++;
      }

      if(occ == 0) {
        return -1;
      }

      if(occ > maxOcc) {
        maxOcc = occ;
      }
      if(occ < minOcc) {
        minOcc = occ;
      }
    }

    score += maxOcc - minOcc;
  }

  for(int i = 0; i < n; i++) {
    if(pos[i] != strings[i].size()) {
      return -1;
    }
  }

  return score;
}

int main() {
  std::string line;

  int numTestCases = 0;
  std::getline(std::cin, line);
  sscanf(line.c_str(), "%d", &numTestCases);

  for(int testCase = 0; testCase < numTestCases; testCase++) {
    int n;

    std::getline(std::cin, line);
    sscanf(line.c_str(), "%d", &n);

    std::vector<std::string> strings;

    for(int i = 0; i < n; i++) {
      std::getline(std::cin, line);
      strings.push_back(line);
    }

    const int result = solveRepeater(strings);

    if(result >= 0) {
      std::cout << "Case #" << (testCase + 1) << ": " << result << std::endl;
    } else {
      std::cout << "Case #" << (testCase + 1) << ": " << "Fegla Won" << std::endl;
    }
  }

  return 0;
}
