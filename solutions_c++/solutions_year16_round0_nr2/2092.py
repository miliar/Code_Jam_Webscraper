#include <cstdio>
#include <cstring>
#include <algorithm>

const int maxn = 105;
const int inf = 0x3f3f3f3f;

char s[maxn];
int f[maxn], g[maxn];

int main() {
  int cas;
  scanf("%d", &cas);
  f[1] = 0;
  g[1] = 1;
  for (int i = 2; i < maxn; ++i) {
    f[i] = 1 + g[i - 1];
    g[i] = 1 + f[i - 1];
  }
  for (int t = 1; t <= cas; ++t) {
    scanf("%s", s);
    int n = strlen(s);
    int m = 0;
    for (int i = 0; i < n; ++i) {
      int j = i;
      while (j + 1 < n && s[i] == s[j + 1]) ++j;
      ++m;
      i = j;
    }
    int ans;
    if (s[0] == '+') ans = f[m];
    else ans = g[m];
    printf("Case #%d: %d\n", t, ans);
  }
  return 0;
}
