#include <algorithm>
#include <functional>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <vector>
using std::cin;
using std::cout;

double Solve(long double C, long double F, long double X) {
  std::vector<long double> K;
  long double current = X / 2.0;

  for (int k = 0;; ++k) {
    long double add = C / (2 + k * F);
    long double prev = (k == 0) ? 0.0 : K.back();
    K.push_back(add + prev);

    long double next = K.back() + X / (2 + (k + 1) * F);
    if (next < current) {
      current = next;
    } else {
      break;
    }
  }

  return current;
}

int main() {
  std::ios_base::sync_with_stdio(false);
//  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/1.txt", "rb", stdin);
  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/B-large.in", "rb", stdin);
  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/B-large.out", "wb", stdout);
  int T;
  cin >> T;

  for (int tc = 0; tc < T; ++tc) {
    double C, F, X;
    cin >> C >> F >> X;

    cout.precision(7);
    cout << "Case #" << tc + 1 << ": " << std::fixed << Solve(C, F, X) << '\n';
  }
  return 0;
}
