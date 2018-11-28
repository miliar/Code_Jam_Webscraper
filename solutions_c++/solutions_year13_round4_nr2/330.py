#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

long long n, p;

void init() {
  cin >> n >> p;
  n = 1LL << n;
}

long long worst_rank(long long mid) {
  long long ret = n, delta = mid - 1, i;
  for (i = 1; delta >= i; i <<= 1) {
    delta -= i;
    ret /= 2;
  }
  return n - ret + 1;
}

long long solve_worst() {
  long long lo = 1, hi = n, mid;
  while (lo + 1 < hi) {
    mid = (lo + hi) / 2;
    if (worst_rank(mid) <= p) {
      lo = mid;
    } else {
      hi = mid;
    }
  }
  if (worst_rank(hi) <= p)
    return hi;
  return lo;
}

long long best_rank(long long mid) {
  long long ret = n, delta = n - mid, i;
  for (i = 1; delta >= i; i <<= 1) {
    delta -= i;
    ret /= 2;
  }
  return ret;
}

long long solve_best() {
  long long lo = 1, hi = n, mid;
  while (lo + 1 < hi) {
    mid = (lo + hi) / 2;
    if (best_rank(mid) <= p) {
      lo = mid;
    } else {
      hi = mid;
    }
  }
  if (best_rank(hi) <= p)
    return hi;
  return lo;
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tcase;
  scanf("%d", &tcase);
  for (int t = 1; t <= tcase; ++t) {
    init();
    printf("Case #%d: ", t);
    cout << solve_worst() - 1 << " "<< solve_best() - 1 << endl;
  }
  return 0;
}
