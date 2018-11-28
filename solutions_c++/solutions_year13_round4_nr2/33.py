#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <cassert>

using namespace std;

const int MAXN = 2005;

int64_t LeastKickOut(int64_t n, int64_t p) {
  if (p >= n) {
    return n;
  }

  if (p <= n / 2) {
    return 1;
  } else {
    int64_t next = LeastKickOut(n / 2, p - n / 2);
    return 1 + next * 2;
  }
}

int64_t BiggerThan(int64_t n, int64_t p) {
  if (p >= n) {
    return 0;
  }

  if (p <= n / 2) {
    int64_t next = BiggerThan(n / 2, p);
    return 1 + next * 2;
  } else {
    int64_t next = BiggerThan(n / 2, p - n / 2);
    return std::min(next, 1ll);
  }
}



void Solve() {
  int n_;
  int64_t n, p;
  cin >> n_ >> p;
  n = 1ll << n_;
  cout << LeastKickOut(n, p) - 1 << " " << n - 1 - BiggerThan(n, p) << endl;
}

int main() {
  int num_cases;
  cin >> num_cases;
  for (int i = 1; i <= num_cases; i++) {
    cout << "Case #" << i << ": ";
    Solve();
  }
}
