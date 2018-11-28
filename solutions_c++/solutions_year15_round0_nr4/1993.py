#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <string>
#include <algorithm>

using namespace std;

typedef long long int lli;

string solve(lli X, lli R, lli C)
{
  if (X >= 7) return "RICHARD";
  else if (X == 1) return "GABRIEL";
  else if (X == 2) return ((R * C) % 2 == 0) ? "GABRIEL" : "RICHARD";
  else {
    if ((R * C) % X == 0 && ((R >= (X-1) && C >= X) || (R >= X && C >= (X-1))))
        return "GABRIEL"; 
    else
        return "RICHARD";
  }
}

int main (int argc, char *argv[])
{
  int64_t T, X, R, C;
  string s;
  cin >> T;
  for(int i = 0; i<T; ++i) {
    cin >> X >> R >> C;
    cout << "Case #" << i+1 << ": ";
    cout << solve(X, R, C);
    cout << endl;
  }

  return 0;
}

