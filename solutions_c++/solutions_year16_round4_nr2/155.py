#include <bits/stdc++.h>
using namespace std;
double prob[205];
double a[205], ans;
double solve() {
  int n, k;
  scanf("%d %d", &n, &k);
  for (int i = 0; i < n; i++) {
    scanf("%lf", &a[i]);
  }
  sort(a, a + n);
  ans = 0.0;
  for (int ii = 0; ii <= k; ii++) {
    memset(prob, 0, sizeof prob);
    prob[0] = 1;
    for (int i = 0; i < ii; i++) {
      for (int j = k - 1; j >= 0; j--) {
        double t = prob[j];
        prob[j + 1] += t * a[i];
        prob[j] *= (1 - a[i]);
      }
    }
    for (int i = n - 1; i >= n - k + ii; i--) {
      for (int j = k - 1; j >= 0; j--) {
        double t = prob[j];
        prob[j + 1] += t * a[i];
        prob[j] *= (1 - a[i]);
      }
    }
    ans = max(ans, prob[k / 2]);
  }
  return ans;
}
int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: %.9lf\n", t, solve());
  }
  return 0;
}

