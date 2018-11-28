#include <bits/stdc++.h>

using namespace std;

const int N = 1005;

char str[N], ans[N + N];

int main() {
  int nt; scanf("%d", &nt);
  for (int caso = 1; caso <= nt; ++caso) {
    scanf("%s", str);
    int begin = N, end = N;
    ans[end++] = str[0];
    for (int i = 1; str[i]; ++i) {
      if (str[i] >= ans[begin]) {
        ans[--begin] = str[i];
      } else {
        ans[end++] = str[i];
      }
    }
    ans[end] = 0;
    printf("Case #%d: %s\n", caso, ans + begin);
  }
  return 0;
}
