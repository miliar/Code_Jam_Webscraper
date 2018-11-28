#include <stdio.h>
#include <vector>

using namespace std;

bool valid(int rows, int columns, int **array) {

  for(int row_count=0; row_count < rows; row_count++) {
    for(int col_count=0; col_count < columns; col_count++) {
      int value = array[row_count][col_count];
      bool found = false;
      for(int i =0; i < rows; i++) {
          if (array[i][col_count] > value) {
              found = true;
              break;
          }
      }
      for(int i =0; i< columns; i++) {
          if (array[row_count][i] > value && found) {
              return false;
          }
      }
    }
  }
  return true;
}

int main() {
  FILE *fp = fopen("input.dat", "r");
  FILE *fout = fopen("output.dat", "w");
  int cases;
  fscanf(fp, "%d\n", &cases);

  int case_count =0;
  for (case_count=0; case_count<cases; case_count++) {
    int rows, columns;
    fscanf(fp, "%d %d\n", &rows, &columns);
    int **array = new int*[rows];
    for(int row_count=0; row_count < rows; row_count++) {
      array[row_count] = new int[columns];
      for(int col_count=0; col_count < columns; col_count++) {
        int value;
        if (col_count==(columns-1)) {
          fscanf(fp, "%d\n", &value);
        } else {
          fscanf(fp, "%d ", &value);
        }
        array[row_count][col_count] = value;
      }
    }
    fprintf(fout, "Case #%d: %s\n", case_count+1, valid(rows,columns, array)?"YES":"NO");
  }
  fclose(fp);
  fclose(fout);

  return 1;
}




