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
  vector<string> Strings;
  for (int i = 0; i < T; ++i)
  {
    std::string S;
    cin >> S;
    Strings.push_back(S);
  }
  for (int i = 0; i < T; ++i)
  {
    std::string maxString = "";
    maxString += Strings[i][0];
    for (int j = 1; j < Strings[i].size(); ++j)
    {
      if (Strings[i][j] < maxString[0]) {
        maxString = maxString + Strings[i][j];
      } else {
        maxString = Strings[i][j] + maxString;
      }
    }
    cout << "Case #" << i+1 << ": " << maxString << endl;
  }
  return 0;
}
