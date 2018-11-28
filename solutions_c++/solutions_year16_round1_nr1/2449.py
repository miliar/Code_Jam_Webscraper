#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <iostream>
using namespace std;

int n, m;
char str[2000], ans[2000];


int main() {
  int T;
  scanf("%d", &T);
  for (int I = 1; I <= T; ++I) {
    scanf("%s", str);
    int len = strlen(str);
    int s = 0, end = len, e = len;
    while (e > 0) {
      // printf("== %d %d\n", s, e);
      char mi = 'A' - 1;
      int index = -1;
      for (int i = e -1; i >= 0; --i) {
        if (index == -1 || mi < str[i]) {
          index = i;
          mi = str[i];
          if (mi == 'Z') break;
        }
      }
      // printf("%d %c\n", s, mi);
      ans[s] = mi;
      ++s;
      for (int i = e - 1; i > index; --i) {
        ans[--end] = str[i];
        // printf("!%d %c\n", i, ans[i]);
      }
      e = index;
      // printf("=# %d %d\n", s, e);
    }
    ans[len] = 0;
    printf("Case #%d: %s\n", I, ans);
  }
}
