/*
 * 
 * File:   pADataPacking.cpp
 * Author: Andy Y.F. Huang (azneye)
 * Created on May 31, 2014, 10:00:42 AM
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

namespace pADataPacking {

void solve(int test_num) {
  static int N, C, size[11111];
  cin >> N >> C;
  for (int i = 0; i < N; i++)
    cin >> size[i];
  sort(size, size + N);
  cout << "Case #" << test_num << ": ";
  for (int i = N; i > 0; i--) {
    bool ok = true;
    for (int j = 0; j < i / 2; j++) {
      if (size[j] + size[i - j - 1] > C) {
        ok = false;
        break;
      }
    }
    if (ok) {
      cout << (N - i / 2) << endl;
      break;
    }
  }
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
  pADataPacking::solve();
  return 0;
}
