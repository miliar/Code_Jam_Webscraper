#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d:", qq);
    int k, c, s;
    scanf("%d %d %d", &k, &c, &s);
    if (c * s < k) {
      puts(" IMPOSSIBLE");
      continue;
    }
    set <long long> z;
    int t = 0;
    for (int i = 0; i < s; i++) {
      long long x = 0;
      for (int j = 0; j < c; j++) {
        x = x * k + t;
        t = (t + 1) % k;
      }
      if (z.find(x) != z.end()) {
        continue;
      }
      z.insert(x);
      printf(" %lld", 1 + x);
    }
    puts("");
  }
  return 0;
}
