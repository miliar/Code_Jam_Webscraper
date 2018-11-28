#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int T, cas = 0;
  scanf("%d", &T);
  while (T --) {
    char s[2000];
    scanf("%s", s);
    string c = "";
    for (int i = 0; s[i]; i ++) {
      if (c + s[i] > s[i] + c) {
        c += s[i];
      } else {
        c = s[i] + c;
      }
    }
    printf("Case #%d: %s\n", ++ cas, c.c_str());
  }
  return 0;
}