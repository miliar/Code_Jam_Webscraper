#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
  int t;
  string S;

  cin >> t; // read number of test cases

  for (int i = 1; i <= t; i++)
  {
    cin >> S; // read in the string s

    string result = S.substr(0,1);
    for (int j = 1; j < S.length(); j++)
    {

      if (S.substr(j, 1).compare(result.substr(0,1)) == 0)
      {
        result = S.substr(j, 1) + result;
      }


      else if (S.substr(j, 1).compare(result) < 0)
      {
        result = result + S.substr(j, 1);
      }

      else
      {
        result = S.substr(j, 1) + result;
      }

    }

    cout << "Case #" << i << ": " << result << endl;
  }
}
