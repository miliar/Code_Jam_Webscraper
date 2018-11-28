#include <stdio.h>

bool is_possible(int *field, int n, int m) {
  int *row_maxs = new int[n];
  int *col_maxs = new int[m];
  for (int i = 0; i < n; ++i) row_maxs[i] = 0;
  for (int i = 0; i < m; ++i) col_maxs[i] = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      int p = i * m + j;
      if (row_maxs[i] < field[p]) row_maxs[i] = field[p];
      if (col_maxs[j] < field[p]) col_maxs[j] = field[p];
    }
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      int p = i * m + j;
      if ((row_maxs[i] > field[p]) && (col_maxs[j] > field[p])) return false;      
    }
  }
  return true;
}

int main(int argc, char const *argv[])
{
  freopen("input.txt", "r", stdin);
  int t;
  scanf("%d\n", &t);
  for (int i = 0; i < t; ++i)
  {
    int n, m;
    scanf("%d%d", &n, &m);
    int *field = new int[n * m];
    for (int j = 0; j < n; j++) {
      for (int k = 0; k < m; k++) {
        scanf("%d", field + j * m + k);
      }
    }
    printf("Case #%d: %s\n", i +1, is_possible(field, n, m) ? "YES" : "NO");
    delete [] field;
  }
  return 0;
}