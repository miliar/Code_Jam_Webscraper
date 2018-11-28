#include<stdio.h>
#include<conio.h>
#include<stdlib.h>




int main()
{
    int t,test=1,i,j, k, col_violated, row_violated;
    int **lawn, n, m;
    
    FILE *file, *out;
    file=fopen("inputSB.txt", "r");
    out=fopen("outputSB.txt", "w");
    fscanf(file,"%d", &t);
    while(test<=t)
    {
               fscanf(file,"%d%d", &n, &m);
               lawn=(int**)malloc(sizeof(int)* n);
               
               for(i=0;i<n;i++)
               lawn[i]=(int*)malloc(sizeof(int)*m);
               
               
               for(i=0;i<n;i++)
               {
                               for(j=0;j<m;j++)
                               fscanf(file,"%d", &lawn[i][j]);
               }
               
               for(i=0;i<n;i++)
               {
                               
                               for(j=0;j<m;j++)
                               {
                                               row_violated=0;
                                               col_violated=0;
                                               for(k=0;k<n;k++)
                                               {
                                                               if(lawn[k][j]>lawn[i][j])
                                                               {
                                                                                col_violated=1;
                                                                                break;
                                                               }
                                               }
                                               if(col_violated==1)
                                               {
                                                                  for(k=0;k<m;k++)
                                                                  {
                                                                  if(lawn[i][k]>lawn[i][j])
                                                                  {
                                                                  row_violated=1;
                                                                  printf("\n\n%d %d", i, k);
                                                                  break;
                                                                  }
                                                                  }
                                                                  if(row_violated)
                                                                  break;
                                               }

                               }
                               
                               if(row_violated==1 && col_violated==1)
                               {
                                                  fprintf(out,"Case #%d: NO\n", test);
                                                  printf("case: %d , violated at %d %d %d", test,i,j,k);
                                                  printf("\n%d %d", row_violated, col_violated);
                                                  break;
                               }
               }
               
               if(row_violated!=1 || col_violated!=1)
               fprintf(out,"Case #%d: YES\n", test);
               
               
               test++;
    }
    
    fclose(file);
    fclose(out);
    
    printf("done");
    
    getch();
    return 0;
}
