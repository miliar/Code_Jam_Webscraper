#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

int compare (char *a, char *b, int &n_a);
int compare (char *a, char *b, int &n_a, char buf[]);

int main ()
{
  FILE *fin, *fout;
  int tests, P, Q, k, j, res;
  char buf[50], a[6], b[6];   
  
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
       for (j = 0; j < 6; j++)
         {
           strcpy (a + j, " ");
           strcpy (b + j, " ");
         }
       fscanf (fin, "%s", buf);
       j = 0;
       while (buf[j] != '/')
         {
           a[j] = buf[j];
           j++;
         }
       j++;
       k = 0;
       while (buf[j] != '\0' && buf[j] != '\n')
         {
           b[k++] = buf[j++];
         }
       P = atoi (a);
       Q = atoi (b);
       
       //printf ("%d %d\n", P, Q);
       
       int temp = Q;
       while (temp > 1) 
         if (temp % 2 == 0) temp /= 2;
         else break;       
       if (temp != 1) res = -1;
       else 
         {
           double temp = (double) Q / (double) P;
           res = 0;
           while (temp > 1)
             {
               temp /= 2;
               res++;
             }
         }
           
       fprintf (fout, "Case #%d: ", i + 1);
       
       if (res >= 0) fprintf (fout, "%d", res);
       else fprintf (fout, "impossible");
       
       if (i != tests - 1) fprintf (fout, "\n");
       
     }

  fclose (fin);
  fclose (fout);
  
  return 0;
}


int compare (char *a, char *b, int &n_a)
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
          if (a[i - 1] == a[i]) 
            {
              n_a++;
              j--;
            }
          else if (b[j - 1] == b[j]) 
            {
              err++;
              i--;
            }
          else 
            {
              //printf ("i = %d, j = %d\n", i, j);
              return -1;
            }
        }
    }
  return err;
}

int compare (char *a, char *b, int &n_a, char buf[])
{
  int err = 0, i, j, bu = 0;
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
          if (a[i - 1] == a[i]) 
            {
              n_a++;
              j--;
            }
          else if (b[j - 1] == b[j]) 
            {
              err++;
              i--;
            }
          else 
            {
              //printf ("i = %d, j = %d\n", i, j);
              return -1;
            }
        }
      else buf[bu++] = a[i];
    }
  return err;
}
