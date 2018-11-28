#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int compare (char *a, char *b);

int main ()
{
  FILE *fin, *fout;
  int tests, N, j, num, res;
  char **a;
  
  if ((fin = fopen ("A-small-attempt1.in", "r")) == NULL)
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
       fscanf (fin, "%d", &N);
       a = new char* [N];
       for (j = 0; j < N; j++)
         a[j] = new char [100];
       for (j = 0; j < N; j++)
         {
           fscanf (fin, "%s", a[j]);
           //printf ("%d %s\n", j, a[j]);
         }
         
       //for (j = 0; j < N; j++)
       //  printf ("%s\n", a[j]);
       
       for (j = 0; j < N - 1; j++)
          {
            res = compare (a[j], a[j + 1]);
            //printf ("res = %d\n", res);
            if (res == -1) 
              {
                num = -1;
                break;
              }
            else num += res;
          }
            
       
       fprintf (fout, "Case #%d: ", i + 1);
       
       if (num >= 0) fprintf (fout, "%d", num);
       else fprintf (fout, "Fegla Won");
       
       if (i != tests - 1) fprintf (fout, "\n");
     }

  fclose (fin);
  fclose (fout);
  
  return 0;
}


int compare (char *a, char *b)
{
  int err = 0, i, j;
  i = 0;
  for (i = 0, j = 0; a[i] != '\0' || b[j] != '\0'; i++, j++)
    {
      /*if (a[i] == '\0' || b[j] == '\0') 
        {
          printf ("i = %d, j = %d\n", i, j);
          return -1;
        }
      */
      if (a[i] != b[j])
        {
          if (i == 0 || j == 0) return -1;
          err++;
          if (a[i - 1] == a[i]) j--;
          else if (b[j - 1] == b[j]) i--;
          else 
            {
              //printf ("i = %d, j = %d\n", i, j);
              return -1;
            }
        }
    }
  return err;
}
