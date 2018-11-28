#include <cstdio>
#include <cstring>
#include <algorithm>

const int N = 1000 + 10;

char s[N];
int k;

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int tid = 1; tid <= tcase; ++tid) {
    scanf(" %s%d", s, &k);
    int n = strlen(s), ans = 0;
    static int a[N];
    for (int i = 0; i < n; ++i) a[i] = (s[i] == '+');
    for (int i = 0; i + k <= n; ++i) {
      if (!a[i]) {
        for (int j = 0; j < k; ++j) a[i + j] ^= 1;
        ++ans;
      }
    }
    printf("Case #%d: ", tid);
    if (std::count(a, a + n, 1) != n) printf("IMPOSSIBLE\n"); else printf("%d\n", ans);
  }
  return 0;
}
