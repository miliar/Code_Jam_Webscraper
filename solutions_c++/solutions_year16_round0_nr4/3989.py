#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int cc = 1; cc <= tt; ++cc) {
    printf("Case #%d: ", cc);
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    printf("%d", 1);
    for (int i = 2; i <= n; ++i) {
      printf(" %d", i);
    }
    printf("\n");
  }
  return 0;
}