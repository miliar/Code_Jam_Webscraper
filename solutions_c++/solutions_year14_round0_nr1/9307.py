
#include <cstdio>
#include <set>
using namespace std;

int main() {
  int T;
  scanf(" %d", &T);
  for (int test = 1; test <= T; ++test) {
    int pos1;
    scanf(" %d", &pos1);

    int mat1[4][4];
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        scanf(" %d", &mat1[i][j]);
      }
    }

    int pos2;
    scanf(" %d", &pos2);

    int mat2[4][4];
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        scanf(" %d", &mat2[i][j]);
      }
    }

    set<int> elems;
    for (int i = 0; i < 4; ++i) {
      elems.insert(mat1[pos1 - 1][i]);
    }

    set<int> possibilities;
    for (int i = 0; i < 4; ++i) {
      int x = mat2[pos2 - 1][i];
      if (elems.find(x) != elems.end()) {
        possibilities.insert(x);
      }
    }

    if (possibilities.size() == 1) {
      printf("Case #%d: %d\n", test, *possibilities.begin());
    } else if (possibilities.size() > 1) {
      printf("Case #%d: Bad magician!\n", test);
    } else {
      printf("Case #%d: Volunteer cheated!\n", test);
    }
  }

  return 0;
}
