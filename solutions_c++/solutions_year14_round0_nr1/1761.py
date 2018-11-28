#include <stdio.h>
#include <algorithm>
#include <iterator>
#include <vector>

void GetOnlyOneRowFrom4By4MatrixInput(int row_number, int row[]) {
  for (int r = 0; r < 4; ++r) {
    for (int c = 0; c < 4; ++c) {
      if (r == row_number) {
        scanf("%d", &row[c]);
      } else {
        int garbage;
        scanf("%d", &garbage);
      }
    }
  }
}

int main() {
  int T = 0;
  scanf("%d", &T);

  std::vector<int> intersection;
  intersection.reserve(4);

  for (int t = 1; t <= T; ++t) {
    int row1 = 1;
    scanf("%d", &row1);
    --row1;
    int row_from_matrix1[4];
    GetOnlyOneRowFrom4By4MatrixInput(row1, row_from_matrix1);
    std::sort(row_from_matrix1, row_from_matrix1 + 4);

    int row2 = 1;
    scanf("%d", &row2);
    --row2;
    int row_from_matrix2[4];
    GetOnlyOneRowFrom4By4MatrixInput(row2, row_from_matrix2);
    std::sort(row_from_matrix2, row_from_matrix2 + 4);

    intersection.clear();
    std::set_intersection(row_from_matrix1, row_from_matrix1 + 4,
                          row_from_matrix2, row_from_matrix2 + 4,
                          std::back_inserter(intersection));

    if (intersection.empty()) {
      printf("Case #%d: Volunteer cheated!\n", t);
    } else if (intersection.size() == 1) {
      printf("Case #%d: %d\n", t, intersection[0]);
    } else {
      printf("Case #%d: Bad magician!\n", t);
    }
  }
  return 0;
}
