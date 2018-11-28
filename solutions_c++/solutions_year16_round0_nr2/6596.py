#include <bits/stdc++.h>

using namespace std;

char s[100100];

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  int T, cas = 0;
  scanf("%d", &T);
  while (T --) {
    scanf("%s", s);
    int n = strlen(s);
    s[n ++] = '+';
    s[n] = 0;
    int ans = 0;
    for (int i = 1; s[i]; i ++) {
      if (s[i] != s[i - 1]) ans ++;
    }
    printf("Case #%d: %d\n", ++ cas, ans);
  }
  return 0;
}