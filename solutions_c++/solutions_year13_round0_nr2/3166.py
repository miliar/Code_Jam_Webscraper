#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

#define MAX 101

int main() {

  int tests;
  scanf(" %d", &tests);
  
  for(int t = 1; t <= tests; t++) {

    int n, m, lawn[MAX][MAX];
    scanf(" %d %d", &n, &m);

    memset(lawn, 0, sizeof(lawn));

    for(int i = 0; i < n; i++)
      for(int j = 0; j < m; j++)
	scanf(" %d", &lawn[i][j]);

    bool possible = true;
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < m; j++) {
	int line_max, col_max;
	line_max = col_max = lawn[i][j];
	for (int k = 0; k < n; k++) 
	  if (lawn[k][j] > line_max) line_max = lawn[k][j];
	for(int k = 0; k < m; k++)
	  if (lawn[i][k] > col_max) col_max = lawn[i][k];
	if (line_max > lawn[i][j] && col_max > lawn[i][j])
	  possible = false;
      }
    }

    printf("Case #%d: ", t);
    printf(possible ? "YES\n" : "NO\n");
  }

  return 0;
}
