#include <cstdio>
#include <vector>

int main() {
  int t, x, y, a1, a2, n, d;
  std::vector<int> r1;
  scanf("%d", &t);
  for (x = 1; x <= t; x++) {
    r1.clear();
    y = 0;
    d = 0;
    scanf("%d", &a1);
    for (int i = 1; i <= 4; i++) {
      for (int j = 1; j <= 4; j++) {
        scanf("%d", &n);
        if (i == a1) {
          r1.push_back(n);
        }
      }
    }
    scanf("%d", &a2);
    for (int i = 1; i <= 4; i++) {
      for (int j = 1; j <= 4; j++) {
        scanf("%d", &n);
        if (i == a2) {
          for (int k = 0; k < 4; k++) {
            if (n == r1[k]) {
              y += n;
              d++;
            }
          }
        }
      }
    }
    printf("Case #%d: ", x);
    if (y == 0) {
      printf("Volunteer cheated!\n");
    } else if (d > 1) {
      printf("Bad magician!\n");
    } else {
      printf("%d\n", y);
    }
  }
  return 0;
}
