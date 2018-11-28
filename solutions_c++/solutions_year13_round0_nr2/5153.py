#include <iostream>
#include <stdio.h>
#include <fstream>

int main ()
{
    freopen ("B-large.in","r",stdin);
    freopen ("B-large.out","w",stdout);
    
    int t, i, j, n, m;
    
    scanf ("%d\n",&t);
    
    for (int trial=1; trial<=t; ++trial)
    {
          scanf ("%d %d\n", &n, &m);
          
          //N is rows
          //M is columns
          
          int garden[n][m];
          
          for (i=0;i<n;++i)
          {
              for (j=0;j<m-1;++j)
              {
                      scanf ("%d ", &garden[i][j]);
              }
              scanf ("%d\n", &garden[i][m-1]);
          }
          /*
          printf ("Grid:\n");
          for (i=0;i<n;++i)
          {
              for (j=0;j<m;++j)
              {
                  printf ("%d ", garden[i][j]);    
              }    
              printf ("\n");
          }*/
          
          //Get the maximum of each row
          int row_max[n];
          for (i=0;i<n;++i)
          {
              row_max[i]=garden[i][0];
              for (j=1;j<m;++j)
              {
                  if (garden[i][j]>row_max[i])
                  {
                     row_max[i] = garden[i][j];                            
                  }    
              }    
          }
          
          //Get the maximum of each column
          int col_max[m];
          for (i=0;i<m;++i)
          {
              col_max[i] = garden[0][i];
              for (j=1;j<n;++j)
              {
                  if (garden[j][i]>col_max[i])
                  {
                     col_max[i] = garden[j][i];                            
                  }
              }    
          }
          
          //Every square must be <= the max in either its row or column
          bool possible = true;
          for (i=0;i<n;++i)
          {
              for (j=0;j<m;++j)
              {
                  if (garden[i][j]<col_max[j] and garden[i][j]<row_max[i])
                  {
                  /*     printf ("%d %d\n", i+1, j+1);
                       printf ("%d %d %d\n", garden[i][j], row_max[i], col_max[j]);  */
                       possible = false;
                       break;                        
                  }    
              } 
              if (!possible)
                 break;
          }
          
          if (possible)
             printf ("Case #%d: YES\n",trial);
          else
              printf ("Case #%d: NO\n",trial);
    }
    
    return 0;   
}
