
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int f(int a, int b, int k) {
  int c = 0;
  for(int j = 0; j < a; j++) {
    for(int i = 0; i < b; i++) {
      if((j & i) < k) {
        c++;
      }
    }
  }

  return c;
}

int main() {
  std::string line;

  int numTestCases = 0;
  std::getline(std::cin, line);
  sscanf(line.c_str(), "%d", &numTestCases);

  for(int testCase = 0; testCase < numTestCases; testCase++) {
    int a, b, k;

    std::getline(std::cin, line);
    sscanf(line.c_str(), "%d %d %d", &a, &b, &k);

    std::cout << "Case #" << (testCase + 1) << ": " << f(a, b, k) << std::endl;
  }
}
