#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1000 + 10;

int main() {
  int T; scanf("%d", &T);
  for (int cas = 1; cas <= T; ++ cas) {
    int n; scanf("%d", &n);
    vector<int> v(n);
    for (int i = 0; i < n; ++ i) scanf("%d", &v[i]);
    int r1 = 0, r2 = 0, rate = 0;
    for (int i = 1; i < n; ++ i) {
      if (v[i] < v[i - 1]) {
        r1 += v[i - 1] - v[i];
        int d = v[i - 1] - v[i];
        rate = max(rate, d);
      }
    }
    for (int i = 0; i + 1 < n; ++ i) {
      r2 += min(v[i], rate);
    }
    printf("Case #%d: %d %d\n", cas, r1, r2);
  }
  return 0;
}
