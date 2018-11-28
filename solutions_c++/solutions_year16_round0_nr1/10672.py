#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>

int main(int argc, char* argv[]) {
  if(argc == 3) {
    freopen(argv[1], "r", stdin);
    freopen(argv[2], "w", stdout);
  }
  int cases;

  std::cin >> cases;
  int numOfCase = 1;

  while(cases--) {
    int init;

    std::cin >> init;
    std::cout << "Case #" << numOfCase << ": ";
    ++numOfCase;

    if (init == 0) {
      std::cout << "INSOMNIA" << std::endl;
      continue;
    }

    int num[10] = {0, };
    int prev = init;
    int cnt = 1;
    int sum = 0;
    bool find = false;

    while (!find) {
      int next = init * cnt;
      std::ostringstream ostr;
      ostr << next;
      std::string nextStr = ostr.str();

      prev = next;

      for (int digit = 0; digit < nextStr.size(); ++digit) {
        if (num[nextStr[digit] - '0'] == 0) {
          num[nextStr[digit] - '0'] = 1;
          ++sum;
        }

        if (sum == 10) {
          find = true;
          break;
        }
      }

      ++cnt;
    }

    std::cout << prev << std::endl;
  }

  return 0;
}
