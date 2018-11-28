#include <bits/stdc++.h>
using namespace std;

void run(int cas) {
  printf("Case #%d:", cas);
  int k, c, s; scanf("%d%d%d", &k, &c, &s);
  if (k > c * s) {puts(" IMPOSSIBLE"); return;}
  for (int i = 0; i < k; ) {
    long long x = 0;
    for (int _ = 0; _ < c && i < k; ++_, ++i) {
      x = x * k + i;
    }
    printf(" %lld", x + 1);
  }
  puts("");
}

int main() {
  int T; scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) run(cas);
  return 0;
}
