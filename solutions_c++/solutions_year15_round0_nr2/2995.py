#include <bits/stdc++.h>
using namespace std;

int main() {
  int test; scanf("%d", &test);
  for (int cas = 1; cas <= test; ++cas) {
    int n; scanf("%d", &n);
    vector<int> xs;
    for (int i = 0; i < n; ++i) {
      int x; scanf("%d", &x);
      xs.push_back(x);
    }
    int u = *max_element(xs.begin(), xs.end());
    int ans = u;
    for (int i = 1; i <= u; ++i) {
      int t = 0;
      for (int x : xs)
        t += (x + i - 1) / i - 1;
      ans = min(ans, t + i);
    }
    printf("Case #%d: %d\n", cas, ans);
  }
  return 0;
}
