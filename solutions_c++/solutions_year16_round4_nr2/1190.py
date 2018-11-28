#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int n, k;
#define eps 1e-9

#define MAX 20
int choice[MAX];

double p[MAX];

double result(int pos, int left, int mask, double prob) {
  if (pos == n) {
    if (left == 0) {
      return prob;
    } else {
      return 0.0;
    }

  } else {
    if (mask & (1 << pos)) {
      return result(pos + 1, left, mask, prob * (1 - p[pos])) +
             (left > 0 ? result(pos + 1, left - 1, mask, prob * p[pos]) : 0.0);
    } else {
      return result(pos + 1, left, mask, prob);
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  int t;
  cin >> t;
  for (int cn = 1; cn <= t; cn++) {
    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
      cin >> p[i];
    }

    double ans = 0;

    if (k % 2 == 0) {
      for (int i = 1; i < (1 << n); ++i) {
        if (__builtin_popcount(i) == k) {
          double cur = result(0, k / 2, i, 1);
          ans = max(cur, ans);
        }
      }
    }

    printf("Case #%d: %.10lf\n", cn, ans);
  }
  return 0;
}
