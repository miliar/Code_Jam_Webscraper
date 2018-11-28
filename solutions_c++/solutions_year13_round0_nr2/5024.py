/*
 * Code Jam Qual 2013 Prob B
 * File:   BLawnmower.cpp
 * Author: Andy Y.F. Huang
 * Created on April 12, 2013, 7:22 PM
 */

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <complex>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>

#ifdef AZN
#include "Azn.cpp"
#endif

using namespace std;

namespace BLawnmower {
int need[111][111];
int highr[111], highc[111];

void solve(int test_num) {
  memset(highr, -1, sizeof (highr));
  memset(highc, -1, sizeof (highc));
  int rows, cols;
  cin >> rows >> cols;
  for (int r = 1; r <= rows; r++)
    for (int c = 1; c <= cols; c++) {
      cin >> need[r][c];
      highr[r] = max(highr[r], need[r][c]);
      highc[c] = max(highc[c], need[r][c]);
    }
  bool ok = true;
  for (int r = 1; r <= rows; r++)
    for (int c = 1; c <= cols; c++)
      if (need[r][c] != highr[r] && need[r][c] != highc[c])
        ok = false;
  printf("Case #%d: %s\n", test_num, ok ? "YES" : "NO");
}

void solve() {
  #ifdef AZN
  freopen("inputB.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  freopen("azn.txt", "w", stderr);
  #endif
  int tests;
  scanf("%d", &tests);
  for (int i = 1; i <= tests; i++)
    solve(i);
}
}

int main() {
  BLawnmower::solve();
  return 0;
}

