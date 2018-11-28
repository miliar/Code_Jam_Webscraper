#include <cstdio>
#include <set>

using namespace std;

int lala[4][4];

void loadall() {
  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      scanf("%d", &lala[i][j]);
    }
  }
}

int main() {
  int T;
  scanf("%d", &T);

  for (int tt = 1; tt <= T; ++tt) {
    int x, y;
    scanf("%d", &x);
    loadall();
    set<int> first, both;
    for (int i = 0; i < 4; ++i) {
      first.insert(lala[x-1][i]);
    }
    scanf("%d", &y);
    loadall();
    for (int i = 0; i < 4; ++i) {
      if (first.count(lala[y-1][i])) {
        both.insert(lala[y-1][i]);
      }
    }
    printf("Case #%d: ", tt);
    if (both.size() > 1) {
      printf("Bad magician!\n");
    } else if (both.size() == 0) {
      printf("Volunteer cheated!\n");
    } else {
      printf("%d\n", *both.begin());
    }
  }
  return 0;
}
