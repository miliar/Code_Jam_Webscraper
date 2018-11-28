#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


const char * DoCase()
{
  int X, R, C;
  cin >> X; cin >> R; cin >> C;
  int cells = R * C;
  if (cells % X != 0)
  {
    return "RICHARD";
  }
  if ((X - 1 > R) || (X - 1 > C))
  {
    return "RICHARD";
  }
  return "GABRIEL";
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


