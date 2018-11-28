#include <stdlib.h>
#include <stdio.h>
#include <math.h>

void heapsort (double *a, int n);

int main ()
{
  FILE *fin, *fout;
  //double ;
  int tests, n, dw, w, j, sub, ind;
  double *a, *b;
  
  if ((fin = fopen ("D-large.in", "r")) == NULL)
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
       fscanf (fin, "%d", &n);
       
       a = new double [n];
       b = new double [n];
       
       for (j = 0; j < n; j++)
         fscanf (fin, "%lf", a + j);
       for (j = 0; j < n; j++)
         fscanf (fin, "%lf", b + j);
       
       fprintf (fout, "Case #%d: ", i + 1);
       
       heapsort (a, n);
       heapsort (b, n);
       
       sub = dw = w = 0;
       
       /*for (j = 0; j < n; j++)
         printf ("%lf ", a[j]);
       printf ("\n");
       for (j = 0; j < n; j++)
         printf ("%lf ", b[j]);
       printf ("\n\n");
       */
       
       ind = 0;
       for (j = 0; j < n; j++)
         if (a[j] < b[ind]) sub++;
         else ind++;
       dw = n - sub;
       
       //printf ("%d\n", dw);
       
       ind = 0;
       sub = 0;
       for (j = 0; j < n; )
         {
           if (a[j] > b[ind]) ;
           else 
             {
               sub++;
               j++;
             }
           ind++;
           //printf (" %d ", j);
           if (ind >= n) break;
         }
       w = n - sub;
       
       //printf ("%d\n", w);
       
       
       fprintf (fout, "%d %d", dw, w);
       
       if (i != tests - 1) fprintf (fout, "\n");
       
       delete [] a;
       delete [] b;
     }

  fclose (fin);
  fclose (fout);
  
  return 0;
}


double *parent (double *a, int k)
{
  return a + (k - 1) / 2;
} 


double *son (double *a, int k)
{
  return a + 2 * k + 1;
}


void heapsort (double *a, int n)
{
  int k, i, pos;
  double *my_parent, *my_son = a, cur, max_child;
  
  for (k = 1; k < n; k++)
    {
      cur = a[k];
      for (i = k; i > 0; )
        {
          my_parent = parent(a, i);
          if (cur > *my_parent) 
            {
              a[i] = *my_parent;
              i = (i - 1) / 2;
            }
          else 
            {
              a[i] = cur;
              break;
            }
        }
      if (i <= 0) a[0] = cur;
    }
  
  for (k = n - 1; k > 0; k--)
    {
      cur = a[k];
      a[k] = a[0];
      a[0] = cur;
      for (i = 0; i * 2 + 1 < k; )
        { 
          my_son = son (a, i);
          if (i * 2 + 2 == k)
            {
              max_child = *my_son;
              pos = i * 2 + 1;
            }
          else 
            {
              if (*my_son >= *(my_son + 1))
                {
                  max_child = *my_son;
                  pos = i * 2 + 1;
                }
              else 
                {
                  max_child = *(my_son +1);
                  pos = i * 2 + 2;
                }
            }
          if (cur < max_child)
            {
              a[i] = max_child;
              i = pos;
            }
          else 
            {
              a[i] = cur;
              break;
            }
        }
      if (i * 2 + 1 >= k) a[i] = cur;
    }
}
