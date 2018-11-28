/*
 *
 * File:   CFairandSquare.cpp
 * Author: Andy Y.F. Huang
 * Created on April 12, 2013, 7:38 PM
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

namespace CFairandSquare {
vector<int> ans;

void solve(int test_num) {
  int from, to, res = 0;
  cin >> from >> to;
  for (int i = 0; i < (int) ans.size(); i++)
    if (from <= ans[i] && ans[i] <= to)
      res++;
  printf("Case #%d: %d\n", test_num, res);
}

void init() {
  static char a[15], b[15];
  for (int i = 1; i * i <= 1000; i++) {
    sprintf(a, "%d", i);
    memcpy(b, a, sizeof (a));
    reverse(b, b + strlen(b));
    if (strcmp(a, b) == 0) {
      sprintf(a, "%d", i * i);
      memcpy(b, a, sizeof (a));
      reverse(b, b + strlen(b));
      if (strcmp(a, b) == 0)
        ans.push_back(i * i);
    }
  }
  //pln(ans);
}

void solve() {
  #ifdef AZN
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  freopen("azn.txt", "w", stderr);
  #endif
  init();
  int tests;
  scanf("%d", &tests);
  for (int i = 1; i <= tests; i++)
    solve(i);
}
}

int main() {
  CFairandSquare::solve();
  return 0;
}

