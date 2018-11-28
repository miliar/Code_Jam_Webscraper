#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <iomanip>
#include <numeric>

using namespace std;

int main() {
  int nTC, tc = 0;
  cin >> nTC;
  while (++tc && nTC--) {
    double C, F, X;
    cin >> C >> F >> X;
    double res = 1e10;
    for (int nFarms = 0; nFarms <= 2000; nFarms++) {
      double candidate = 0;
      for (int i = 0; i < nFarms; i++) {
        candidate += C / (2.0 + i * F);
      }
      candidate += X / (2.0 + nFarms * F);
      if (candidate < res) {
        res = candidate;
      }
    }
    printf("Case #%d: %.8lf\n", tc, res);
  }
  return 0;
}

