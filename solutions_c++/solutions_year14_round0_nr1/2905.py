#include <cstdio>
using namespace std;

int main() {
  FILE *fin = fopen("A-small-attempt0.in", "r");
  FILE *fout = fopen("A-small-attempt0.out", "w");
  int testnum = 0;
  fscanf(fin, "%d", &testnum);
  for (int test = 1; test <= testnum; ++test) {
    int matrix1[4][4];
    int matrix2[4][4];
    int ans1, ans2;
    fscanf(fin, "%d", &ans1);
    ans1--;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        fscanf(fin, "%d", &matrix1[i][j]);
      }
    }
    fscanf(fin, "%d", &ans2);
    ans2--;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        fscanf(fin, "%d", &matrix2[i][j]);
      }
    }
    int curans = -1;
    int found = 0;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        if (matrix1[ans1][i] == matrix2[ans2][j]) {
          ++found;
          curans = matrix1[ans1][i];
        }
      }
    }
    fprintf(fout, "Case #%d: ", test);
    if (found == 0) {
      fprintf(fout, "Volunteer cheated!\n");
      continue;
    }
    if (found > 1) {
      fprintf(fout, "Bad magician!\n");
      continue;
    }
    fprintf(fout, "%d\n", curans);
  }

}