#include <bits/stdc++.h>
using namespace std;
char t[] = "11111111111111111111111111111111111111111111111111111111111111";
char s[100];
void solve() {
  int n, l;
  scanf("%d %d", &n, &l);
  bool ok = true;
  for (int i = 0; i < n; i++) {
    scanf("%s", s);
    if (strncmp(s, t, l) == 0) {
      ok = false;
      
    }
  }
  scanf("%s", s);
  if (!ok) {
     printf("IMPOSSIBLE");
  } else {
    for (int i = 0; i < l - 1; i++) {
      printf("01");
    }
    printf("0 ");
    for (int i = 0; i < l; i++) {
      printf("0?");
    }
  }
}
int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    solve();
    printf("\n");
  }
  return 0;
}

