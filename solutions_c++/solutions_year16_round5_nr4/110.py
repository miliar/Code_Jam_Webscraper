#include <bits/stdc++.h>
using namespace std;

int main() {
  int t, n, m;
  scanf("%d", &t);
  char c[10005];
  for (int cs = 1; cs <= t; cs++) {
    scanf("%d %d", &n, &m);
    set<string> ss;
    for (int i = 0; i < n; i++) {
      scanf("%s", c);
      string sss = c;
      ss.insert(sss);
    }
    string s;
    scanf("%s", c);
    s = c;
    printf("Case #%d: ", cs);
    if (ss.find(s) != ss.end()) {
      printf("IMPOSSIBLE\n");
    } else {
      if (m != 1) {
        for (int i = 0; i < m; i++) {
          printf("0?");
        }
        printf(" ");
        for (int i = 0; i < m - 1; i++) {
          printf("1");
        }
        printf("\n");
      } else {
        printf("0 ?\n");
      }
    }

  }
  
}

