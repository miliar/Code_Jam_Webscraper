#include <cassert>
#include <cstdio>

#include <algorithm>
using namespace std;

const long double eps = 1e-12;

int main () {
  int tn;
  assert (scanf ("%d", &tn) == 1);
  for (int tt = 1; tt <= tn; tt++) {
    int n;
    long double V, T;
    assert (scanf ("%d%Lf%Lf", &n, &V, &T) == 3);
    long double v[n], t[n];
    for (int i = 0; i < n; i++)
      assert (scanf ("%Lf%Lf\n", &v[i], &t[i]) == 2);
    bool leq = true, meq = true, equal = false;
    for (int i = 0; i < n; i++) {
      if (t[i] < T - eps)
        meq = false;
      else if (t[i] > T + eps)
        leq = false;
      else
        equal = true;
    }
    if (equal) {
      long double speed = 0.0;
      for (int i = 0; i < n; i++)
        if (T - eps <= t[i] && t[i] <= T + eps)
          speed += v[i];
      long double ans = V / speed;
      printf ("Case #%d: %.20Lf\n", tt, ans);
      continue;
    }
    if (meq || leq) {
      printf ("Case #%d: IMPOSSIBLE\n", tt);
      continue;
    }
    long double alpha = (T - t[1]) / (t[0] - t[1]);
    long double beta = (T - t[0]) / (t[1] - t[0]);
    alpha /= v[0];
    beta /= v[1];
    long double k = max (alpha, beta);
    alpha /= k;
    beta /= k;
    long double speed = v[0] * alpha + v[1] * beta;
    long double ans = V / speed;
    printf ("Case #%d: %.20Lf\n", tt, ans);
  }
  return 0;
}

