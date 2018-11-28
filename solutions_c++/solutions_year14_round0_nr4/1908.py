#include <cassert>
#include <cstdio>
#include <algorithm>

int main() {
  using std::sort;
  int tn;
  assert(scanf("%d", &tn) == 1);
  for (int t = 1; t <= tn; t++) {
    int n;
    assert(scanf("%d", &n) == 1);
    double a[n], b[n];
    for (int i = 0; i < n; i++)
      assert(scanf("%lf", &a[i]) == 1);
    for (int i = 0; i < n; i++)
      assert(scanf("%lf", &b[i]) == 1);
    sort(a, a + n);
    sort(b, b + n);
    int l = 0, r = n - 1;
    int score_min = 0;
    for (int i = n - 1; i >= 0; i--) {
      if (a[i] < b[r])
        r--;
      else {
        l++, score_min++;
      }
    }
    int score_max = 0;
    for (int i = 0; i <= n; i++) {
      bool ok = true;
      for (int j = 0; j < i; j++)
        if (a[j + n - i] < b[j])
          ok = false;
      if (ok)
        score_max = i;
    }
    printf("Case #%d: %d %d\n", t, score_max, score_min);
  }
  return 0;
}

