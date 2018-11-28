#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main ()
{
  FILE *fin, *fout;
  int tests;
  int A, B, K, num;
  
  if ((fin = fopen ("B-small-attempt0.in", "r")) == NULL)
    {
      return -1;
    }
  if ((fout = fopen ("output.txt", "w")) == NULL)
    {
      fclose (fin);
      return -1;
    }

  fscanf (fin, "%d", &tests);
  
  for (int i = 0; i < tests; i++)
    {
       fscanf (fin, "%d%d%d", &A, &B, &K);
                
       fprintf (fout, "Case #%d: ", i + 1);
       num = 0;
       for (int j = 0; j < A; j++)
         for (int l = 0; l < B; l++)
           {
             //printf ("%d %d %d\n", 
             if ((j & l) < K) num++;
           }
         
       fprintf (fout, "%d", num);
       
       if (i != tests - 1) fprintf (fout, "\n");
     }

  fclose (fin);
  fclose (fout);
  
  return 0;
}
