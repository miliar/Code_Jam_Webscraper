#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <string.h>

using namespace std;

int main()
{
  unsigned int T;
  cin >> T;
  vector<uint64_t> numbers;
  for (int i = 0; i < T; ++i)
  {
    uint64_t N;
    cin >> N;
    numbers.push_back(N);
  }
  for (int i = 0; i < T; ++i)
  {
    uint64_t N = numbers[i];
    bool usedNumber[10];
    for (int j = 0; j < 10; ++j)
    {
      usedNumber[j] = false;
    }
    if (N == 0) {
      cout << "Case #" << i+1 << ": INSOMNIA" << endl;
      continue;
    }
    bool hasUsedAllNumbers = false;
    uint64_t x = 1;
    uint64_t lastXN = N;
    while (!hasUsedAllNumbers) {
      uint64_t xN = x * N;
      lastXN = xN;
      while (xN != 0) {
        int digit = xN % 10;
        xN = xN / 10;
        usedNumber[digit] = true;
      }
      bool hasOneFalse = false;
      for (int j = 0; j < 10; ++j)
      {
        if (!usedNumber[j]) {
          hasOneFalse = true;
        }
      }
      if (!hasOneFalse) {
        hasUsedAllNumbers = true;
      }
      x++;
    }
    cout << "Case #" << i+1 << ": " << lastXN << endl;
  }
  return 0;
}
