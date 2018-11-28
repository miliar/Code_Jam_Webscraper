/*
 * 
 * File:   pBUpandDown.cpp
 * Author: Andy Y.F. Huang (azneye)
 * Created on May 31, 2014, 10:14:28 AM
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

using namespace std;

namespace pBUpandDown {
int a[1111], b[1111];
int N;

void solve(int test_num) {
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> a[i];
    b[i] = a[i];
  }
  sort(b, b + N);
  int res = 0;
  for (int i = 0; i < N; i++) {
    const int pos = find(a, a + N, b[i]) - a;
    int lef = 0, rig = 0;
    for (int j = pos - 1; j >= 0; j--)
      if (a[j] > b[i])
        lef++;
    for (int j = pos + 1; j < N; j++)
      if (a[j] > b[i])
        rig++;
    res += min(lef, rig);
  }
  cout << "Case #" << test_num << ": " << res << endl;
}

void solve() {
#ifdef AZN
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  freopen("azn.txt", "w", stderr);
#endif
  int tests;
  cin >> tests;
  for (int i = 1; i <= tests; i++)
    solve(i);
}
}

int main() {
  pBUpandDown::solve();
  return 0;
}
