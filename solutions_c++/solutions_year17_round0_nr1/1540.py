#include<bits/stdc++.h>

using namespace std;

char ch[2222];

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int T, cas = 1; scanf("%d", &T);
  while (T --) {
    int k;
    scanf("%s%d", ch, &k);
    int ans = 0, len = strlen(ch);
    for (int i = 0; i <= len - k; i ++) {
      if (ch[i] == '-') {
        ans ++;
        for (int j = i; j < i + k; j ++) {
          if (ch[j] == '-') ch[j] = '+';
          else ch[j] = '-';
        }
      }
    }
    for (int i = len - k; i < len; i ++) {
      if (ch[i] == '-') ans = -1;
    }
    printf("Case #%d: ", cas ++);
    if (ans == -1) puts("IMPOSSIBLE");
    else printf("%d\n", ans);
  }
  return 0;
}
