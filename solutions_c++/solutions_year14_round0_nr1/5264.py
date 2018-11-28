#include <cstdio>
#include <vector>
using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    int a1;
    vector<bool> m1(20, false);
    vector<bool> m2(20, false);
    scanf("%d", &a1); a1--;
    for (int y = 0; y < 4; y++) for (int x = 0; x < 4; x++) {
      int w;
      scanf("%d", &w);
      if (y == a1) m1[w] = true;
    }
    scanf("%d", &a1); a1--;
    for (int y = 0; y < 4; y++) for (int x = 0; x < 4; x++) {
      int w;
      scanf("%d", &w);
      if (y == a1) m2[w] = true;
    }
    int count = 0, res = 0;
    for (int r = 1; r <= 16; r++) {
      if (m1[r] && m2[r]) res = r, count++;
    }
    printf("Case #%d: ", tc);
    if (count == 0) printf("Volunteer cheated!\n");
    else if (count > 1) printf("Bad magician!\n");
    else printf("%d\n", res);
  }
}
