#include <cstdio>
#include <climits>

int n, m;
int lawn[105][105];

bool possible() {
   int min_col[105];
   int min_row[105];
   int max_col[105];
   int max_row[105];
   bool col_all_same[105];
   bool row_all_same[105];
   bool row_possible = true;
   bool col_possible = true;

   for (int i = 0; i < 105; i++) {
      col_all_same[i] = true;
      row_all_same[i] = true;
   }

   for (int i = 0; i < n; i++) {
      min_row[i] = INT_MAX;
      max_row[i] = 0;
      for (int j = 0; j < m; j++) {
         if (j > 0 && lawn[i][j] != lawn[i][j-1]) row_all_same[i] = false;
         if (lawn[i][j] < min_row[i]) min_row[i] = lawn[i][j];
         if (lawn[i][j] > max_row[i]) max_row[i] = lawn[i][j];
      }
   }

   for (int j = 0; j < m; j++) {
      min_col[j] = INT_MAX;
      max_col[j] = 0;
      for (int i = 0; i < n; i++) {
         if (i > 0 && lawn[i][j] != lawn[i-1][j]) col_all_same[j] = false;
         if (lawn[i][j] < min_col[j]) min_col[j] = lawn[i][j];
         if (lawn[i][j] > max_col[j]) max_col[j] = lawn[i][j];
      }
   }


   for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
         if (lawn[i][j] < max_row[i]) {
            if (lawn[i][j] == min_col[j] && !col_all_same[j]) {
               row_possible = false;
            }
         }
      }
   }

   for (int j = 0; j < m; j++) {
      for (int i = 0; i < n; i++) {
         if (lawn[i][j] < max_col[i]) {
            if (lawn[i][j] == min_row[i] && !row_all_same[i]) {
               col_possible = false;
            }
         }
      }
   }

   return (row_possible);
}

int main() {
   int t;
   scanf("%d", &t);

   for (int i = 0; i < t; i++) {
      scanf("%d %d", &n, &m);

      for (int j = 0; j < n; j++) {
         for (int k = 0; k < m ;k++) {
            scanf("%d", &lawn[j][k]);
         }
      }

      printf("Case #%d: ", i+1);
      if (possible()) {
         printf("YES\n");
      } else {
         printf("NO\n");
      }

   }
}
