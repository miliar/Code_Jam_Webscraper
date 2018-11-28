#include <cstdio>
#include <set>
using namespace std;

set <int> appear;

int main() {
  int Case;
  scanf("%d", &Case);
  for (int c = 1; c <= Case; ++ c) {
    appear.clear();
    int n, d;
    scanf("%d", &n);
    for (int i = 1; i <= 4; ++ i) {
      for (int j = 1; j <= 4; ++ j) {
        scanf("%d", &d);
        if (n == i) {
          appear.insert(d);
        }
      }
    }
    int ans, ans_n = 0;
    scanf("%d", &n);
    for (int i = 1; i <= 4; ++ i) {
      for (int j = 1; j <= 4; ++ j) {
        scanf("%d", &d);
        if (n == i) {
          if (appear.find(d) != appear.end()) {
            ++ ans_n;
            ans = d;
          }
        }
      }
    }
    printf("Case #%d: ", c);
    if (ans_n == 0) {
      printf("Volunteer cheated!\n");
    } else if (ans_n == 1) {
      printf("%d\n", ans);
    } else {
      printf("Bad magician!\n");
    }
  }
  return 0;
}
