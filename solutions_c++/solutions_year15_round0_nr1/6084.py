#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

#define I(x) (x-'0')

int DoCase()
{
  int Smax, standup;
  string S;
  int friends = 0;
  cin >> Smax;
  cin >> S;
  standup = I(S[0]);
  for (int i = 1; (i <= Smax) && (standup < Smax); i++)
  {
    int si = I(S[i]);
    if ((si > 0) && (i > standup))
    {
      int addfriends = (i - standup);
      friends += addfriends;
      standup += addfriends;
    }
    standup += si;
  }
  return friends;
}


int main()
{
  int t, T;
  cin >> T;
  for (t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": " << DoCase() << '\n';
  }
  return 0;
}

