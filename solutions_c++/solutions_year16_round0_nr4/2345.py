#include <bits/stdc++.h>

using namespace std;

int main() {
#ifdef DEBUG
  freopen("input.txt", "rt", stdin);
#else
  freopen("D-small.in", "rt", stdin);
  freopen("D-small.out", "wt", stdout);
#endif
  int t; scanf("%d", &t);
  for(int tst = 1; tst <= t; ++tst) {
    int k, c, s; scanf("%d %d %d", &k, &c, &s);
    assert(k == s);
    printf("Case #%d:", tst);
    for(int i = 1; i <= k; ++i) {
      printf(" %d", i);
    }
    putchar('\n');
  }
  return 0;
}
