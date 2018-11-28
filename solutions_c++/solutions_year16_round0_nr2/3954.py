#include <bits/stdc++.h>

using namespace std;

char str[105];

int main() {
  int nt; scanf("%d", &nt);
  for (int caso = 1; caso <= nt; ++caso) {
    scanf("%s", str);
    int cnt = 0;
    for (int i = 0, n = strlen(str); i < n; ++i) {
      if (str[i] == '-') {
        ++cnt;
        while (i < n && str[i] == '-') ++i;
      }
    }

    printf("Case #%d: %d\n", caso, cnt * 2 - (str[0] == '-'));
  }
  return 0;
}