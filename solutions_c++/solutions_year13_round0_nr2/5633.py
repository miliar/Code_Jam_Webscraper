#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

int a[105][105] = {0};

FILE *fpd = NULL;
int main ()
{
    int T, N, M;
    
    FILE *fpI = fopen("B-large.in", "r");
    FILE *fpO = fopen("output.txt", "w+");
    
    fpd = fopen("debug.txt", "w+");
    
    
    fscanf(fpI, "%d", &T);
    fprintf(fpd, "%d\n", T);
    for (int i = 0; i < T; i++)
    {

        int min_col = 0;
        int max_col = 0;
        int not_possible = 0;
        fscanf(fpI, "%d %d", &N, &M);
        
        fprintf(fpd, "\nN = %d, M = %d\n", N, M);

        for (int j = 0; j < N; j++) {
            for (int k = 0; k < M; k++) {
               fscanf(fpI, "%d", &a[j][k]);
               
               if (j == 0) {
                     a[N][k] = a[0][k];
                     a[N+1][k] = a[0][k];
               }
               
               if (k == 0) {
                     a[j][M] = a[j][0];
                     a[j][M+1] = a[j][0];
                     //fprintf(fpd, "%d ", a[j][k]);
                     //continue;
               }
                              
               if (a[j][M] > a[j][k])
               {
                   a[j][M] = a[j][k];
               }
               if (a[j][M+1] < a[j][k])
               {
                   a[j][M+1] = a[j][k];
               }
               if (a[N][k] > a[j][k]) {
                   a[N][k] = a[j][k];
               }
               if (a[N+1][k] < a[j][k]) {
                   a[N+1][k] = a[j][k];
               }
               fprintf(fpd, "%d ", a[j][k]);
            }
            fprintf(fpd, "\nmin_row(%d) = %d, max_row(%d) = %d\n", j, a[j][M], j, a[j][M+1]);
        }
        
        fprintf(fpd, "\n\n\n");
        
        for (int k = 0; k < M; k++) {
            fprintf(fpd, "\nmin_col(%d) = %d, max_col(%d) = %d", k, a[N][k], k, a[N+1][k]);
        }
        
        for (int j = 0; j < N; j++) {
            if (a[j][M] == a[j][M+1]) {
               /* No Problem for this row */
               continue;
            }
            
            for (int k = 0; k < M; k++) {
                if (a[j][k] < a[j][M+1]) {
                      if (a[j][k] == a[N+1][k])
                      {
                           /* No Problem for this cell */
                      }
                      else {
                           not_possible = 1;
                           break;
                      }
                }
            }
            
            if (not_possible == 1)
            {
               break;
            }
        }
        
        fprintf(fpO, "Case #%d: %s\n", (i+1), (not_possible)? "NO": "YES");
   }
}

