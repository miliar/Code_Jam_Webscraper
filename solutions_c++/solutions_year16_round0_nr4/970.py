#include "stdafx.h"

#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
#include <array>
#include <set>

using namespace std;



void testcase(const int casenum)
{
  int K, S, C;
  cin >> K >> C >> S;
  std::cout << "Case #" << casenum << ":";

  /*std::vector<__int64> powers(C + 1);
  __int64 K64 = K;
  powers[0] = 1;

  for (int i = 1; i <= C; ++i)
  {
    powers[i] = powers[i - 1] * K64;
  }*/

  int nrAttempts = K % C == 0 ? K / C : K / C + 1;

  if (nrAttempts > S)
  {
    cout << " IMPOSSIBLE" << endl;
    return;
  }

  for (int i = 0; i < nrAttempts; ++i)
  {
    int startPos = i * C + 1;
    __int64 pos = startPos;
    for (int j = startPos + 1; j <= std::min((i + 1) * C, K); ++j)
    {
      pos = (pos - 1) * K + j;
    }
    cout << " " << pos;
  }
  
  cout << endl;
}

int main()
{
  int n;
  std::cin >> n;

  for (int i = 1; i <= n; i++)
  {
    testcase(i);
  }

  return 0;
}