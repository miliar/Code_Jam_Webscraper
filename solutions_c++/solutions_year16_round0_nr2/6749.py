#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int t = 0; t < T; t++)
  {
    string str;
    cin >> str;
    int bitFlip = 0;
    int nFlip = 0;
    for (int i = str.length() - 1; i >= 0; i--)
    {
      int bit;
      if (str[i] == '-')
      {
        bit = 0 ^ bitFlip;
      }
      else
      {
        bit = 1 ^ bitFlip;
      }
      if (!bit)
      {
      	bitFlip = !bitFlip;
      }
      nFlip += !bit;
    }
    cout << "Case #" << t + 1 << ": " << nFlip << endl;
  }
  return 0;
}