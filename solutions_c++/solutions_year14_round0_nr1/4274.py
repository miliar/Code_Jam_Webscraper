#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int equal (int a[], int b[]);

int main ()
{
  FILE *fin, *fout;
  int tests, row, j, k, temp, card, num = 0;
  int a[4], b[4];
  
  if ((fin = fopen ("A-small-attempt0.in", "r")) == NULL)
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
       num = 0;
       fscanf (fin, "%d", &row);
       for (j = 0; j < 16; j++)
         {
           fscanf (fin, "%d", &temp);
           if (j / 4 == row - 1) a[j % 4] = temp;
         }
       fscanf (fin, "%d", &row);
       for (j = 0; j < 16; j++)
         {
           fscanf (fin, "%d", &temp);
           if (j / 4 == row - 1) b[j % 4] = temp;
         }
         
       fprintf (fout, "Case #%d: ", i + 1);
       
       for (j = 0; j < 4; j++)
         {
           if (equal (a + j, b) == 1) { card = a[j]; num++; }
         }
         
       if (num == 1) fprintf (fout, "%d", card);
       else if (num > 1) fprintf (fout, "Bad magician!");
       else fprintf (fout, "Volunteer cheated!");
       
       if (i != tests - 1) fprintf (fout, "\n");
     }

  fclose (fin);
  fclose (fout);
  
  return 0;
}


int equal (int a[], int b[])
{
  for (int i = 0; i < 4; i++)
    if (a[0] == b[i]) return 1;
  return 0;
}
