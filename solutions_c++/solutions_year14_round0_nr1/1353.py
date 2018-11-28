#include <iostream>
#include <set>
using namespace std;
int main() {
  int tc;
  scanf("%d", &tc);
  for (int cas = 1; cas <= tc; ++cas) {
    set<int> s;
    int r;
    int a[4][4];
    scanf("%d", &r);
    for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j) scanf("%d", &a[i][j]);
    for (int i = 0; i < 4; ++i) s.insert(a[r - 1][i]);
    scanf("%d", &r);
    for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j) scanf("%d", &a[i][j]);
    int p = -1;
    for (int i = 0; i < 4; ++i) {
      int x = a[r - 1][i];
      if (s.find(x) != s.end()) {
        if (p > 0) p = -2;
        else if (p == -1) p = x;
      }
    }
    printf("Case #%d: ", cas);
    if (p == -2) printf("Bad magician!\n");
    else if (p == -1) printf("Volunteer cheated!\n");
    else printf("%d\n", p);
  }
  return 0;
}
