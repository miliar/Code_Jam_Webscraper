#include <cstdio>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {
  int t, row;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    scanf("%d", &row);
    vector<int> row1(4,0);
    vector<int> row2(4,0);
    for (int j = 0; j < 4; j++) {
      int r[4];
      scanf("%d %d %d %d\n", &r[0], &r[1], &r[2], &r[3]);
      if (j + 1 == row) {
        row1[0] = r[0];
        row1[1] = r[1];
        row1[2] = r[2];
        row1[3] = r[3];
      }
    }
    scanf("%d", &row);
    for (int j = 0; j < 4; j++) {
      int r[4];
      scanf("%d %d %d %d\n", &r[0], &r[1], &r[2], &r[3]);
      if (j + 1 == row) {
        row2[0] = r[0];
        row2[1] = r[1];
        row2[2] = r[2];
        row2[3] = r[3];
      }
    }
    int match = -1, n = 0;
    for (size_t j = 0; j < 4; j++) {
      for (size_t k = 0; k < 4; k++) {
        if (row1[j] == row2[k]) {
          match = row1[j];
          n++;
        }
      }
    }
    printf("Case #%d: ", i);
    if (n == 1) {
      printf("%d\n", match);
    } else if (n == 0) {
      printf("Volunteer cheated!\n");
    } else {
      printf("Bad magician!\n");
    }
  }
  return 0;
}
