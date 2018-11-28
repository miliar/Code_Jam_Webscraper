#include <cstdio>
#include <set>

using namespace std;

void init() {
  set<int> row1;
  int currow;
  scanf("%d", &currow);
  for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <=4; j++) {
      int cur;
      scanf("%d", &cur);
      if (i == currow) {
        row1.insert(cur);
      }
    }
  }
  scanf("%d", &currow);
  int find = -1;
  for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <=4; j++) {
      int cur;
      scanf("%d", &cur);
      if (i == currow) {
        if (row1.find(cur) != row1.end()) {
          if (find > 0) {
            find = 17;
          } else {
            find = cur;
          }
        }
      }
    }
  }
  if (find == 17) {
    printf("Bad magician!\n");
    return;
  }
  if (find < 0) {
    printf("Volunteer cheated!\n");
    return;
  }
  printf("%d\n", find);
  return;
}

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int i = 1; i <= tcase; i++) {
    printf("Case #%d: ", i);
    init();
  }
  return 0;
}
