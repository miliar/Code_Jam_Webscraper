#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int flips(string str)
{
  int n = str.length();
  char which = str[0];
  int flips = 0;
  for (int i = 1; i < n; ++i)
  {
    if (str[i] != which)
    {
      which = str[i];
      ++flips;
    }
  }
  if (which == '-')
    ++flips;
  return flips;
}

int main()
{
  int T;
  cin >> T;

  string garbage;
  getline(cin, garbage);
  
  for (int t = 1; t <= T; ++t)
  {
    string str;
    getline(cin, str);
    cout << "Case #" << t << ": " << flips(str) << endl;
  }
}
