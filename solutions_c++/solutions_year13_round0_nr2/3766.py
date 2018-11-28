#include <cstdio>
#include <cstdlib>

int lawn[105][105];
int heighestRow[105];
int heighestCol[105];

int n, m;
FILE *fin = fopen ("input.txt", "r");
FILE *fout = fopen ("output.txt", "w");

bool checkLawn (void);
void scanBoard (int n, int m);
void scanHeighest (void);

int main (int argc, char **argv) {
   int t;
   fscanf (fin, "%d", &t);
   
   for (int i = 0; i < t; i++) {
      fscanf (fin, "%d %d", &n, &m);
      scanBoard (n, m);
      scanHeighest ();
      if (checkLawn ()) {
         fprintf (fout, "Case #%d: YES\n", i + 1);
      } else {
         fprintf (fout, "Case #%d: NO\n", i + 1);
      }
   }
   
   return 0;
}

bool checkLawn (void) {
   for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
         if (lawn[i][j] < heighestRow[i] && lawn[i][j] < heighestCol[j]) {
            //printf ("n = %d, m = %d\n", n, m);
            //printf ("failed on lawn[%d][%d] = %d failing heighestRow[%d] = %d and heighestCol[%d] = %d\n", i, j, lawn[i][j], i, heighestRow[i], j, heighestCol[j]);
            //system ("pause");
            return false;
         }
      }
   }
   return true;
}

void scanBoard (int n, int m) {
   for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
         fscanf (fin, "%d", &lawn[i][j]);
      }
   }
}

void scanHeighest (void) {
   for (int i = 0; i < 105; i++) {
      heighestRow[i] = 0;
      heighestCol[i] = 0;
   }
   
   for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
         if (lawn[i][j] > heighestRow[i]) {
            heighestRow[i] = lawn[i][j];
         }
      }
   }
   
   for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
         if (lawn[j][i] > heighestCol[i]) {
            heighestCol[i] = lawn[j][i];
         }
      }
   }
}
