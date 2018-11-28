#include <iostream>
#include <set>
#include <algorithm>
#include "num.h"

using namespace std;

int divisor(const Num &value) {
  auto lim = 1000;
  if (value < lim) {
    lim = value.back();
  }
  for (int k = 2; k < lim; ++k) {
    if (value % k == 0) {
      return k;
    }
  }
  return 0;
}

int main()
{
  int cases;
  cin >> cases;
  int n, j;
  cin >> n >> j;

  auto startNum = Num(2).pow(n - 1);
  ++startNum;

  cout << "Case #1:" << endl;
  while (j > 0) {
    std::vector<char> binNum;
    startNum.print(binNum, 2);

    bool found = true;
    for(int base = 2; base <= 10; ++base) {
      auto curNam = Num(&binNum[0], base);
      if (!divisor(curNam)) {
        found = false;
        break;
      }
    }

    if (found) {
      string val(&binNum[0]);
      cout << val;
      for(int base = 2; base <= 10; ++base) {
        auto curNam = Num(&binNum[0], base);
        auto div = divisor(curNam);
        cout << " " << div;
      }
      cout << endl;
      --j;
    }
    startNum += 2;
  }
}
