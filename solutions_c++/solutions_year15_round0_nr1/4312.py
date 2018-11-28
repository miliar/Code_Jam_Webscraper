#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <string>
#include <algorithm>

using namespace std;

int64_t solve(int64_t Smax, const string& s)
{
  int64_t sum = 0, diff = 0;
  for (int i = 0; i <= Smax; ++i) {
    if (i > sum) { diff += (i - sum); sum = i; }
    sum += (s[i] - '0');
  }
  return diff;
}

int main (int argc, char *argv[])
{
  int64_t T, Smax;
  string s;
  cin >> T;
  for(int i = 0; i<T; ++i) {
    cin >> Smax >> s;
    cout << "Case #" << i+1 << ": ";
    cout << solve(Smax, s);
    cout << endl;
  }

  return 0;
}

