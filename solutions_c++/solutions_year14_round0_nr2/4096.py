#include <cassert>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <numeric>
#include <sstream>
#include <utility>

#include <algorithm>
#include <bitset>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#include <memory.h>
using namespace std;

#pragma comment(linker, ”/STACK:108777216“)

#define Pi 3.141592653589793
#define all(c) (c).begin(), (c).end()
typedef long long ll;

int ri() {
  int res; scanf("%d", &res); return res;
}

class timer {
public:
  timer() : t_(clock()) {}
  void start() { t_ = clock(); }
  float elapsed() { return float(clock() - t_) / CLOCKS_PER_SEC; }
private:
  clock_t t_;
};

bool pos(double C, double F, double X, double t) {
  double v = 2.0;
  for (int i = 0; i <= 100000 && t >= 0.0; ++i) {
    if (v * t >= X) {
      return true;
    }
    t -= C / v;
    v += F;
  }
  return false;
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int T; cin >> T;
  for (int qq = 1; qq <= T; ++qq) {
    cout << "Case #" << qq << ": ";
    double C, F, X; cin >> C >> F >> X;
    double lo = 0;
    double hi = X;
    for (int i = 0; i < 100; ++i) {
      double mi = (lo + hi) * 0.5;
      if (pos(C, F, X, mi)) {
        hi = mi;
      } else {
        lo = mi;
      }
    }
    printf("%.9f\n", (lo + hi) * 0.5);
  }

  return 0;
}
