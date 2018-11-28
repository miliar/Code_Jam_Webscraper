#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main ()
{
  FILE *fin, *fout;
  double C, F, X, global_sec, sec1, sec2, own, mps, med;
  int tests;
  
  if ((fin = fopen ("B-large.in", "r")) == NULL)
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
       fscanf (fin, "%lf%lf%lf", &C, &F, &X);
                
       fprintf (fout, "Case #%d: ", i + 1);
       
       global_sec = 0.;
       own = 0.;
       mps = 2.;
       while ((X - own) > 1e-7)
         {
           med = ((X > C) ? C : (X - own));
           if (own >= C)
             {
               //if (fabs (own - C) > 1e-7) printf (" ! ");
               sec1 = (X - own) / mps;
               sec2 = X / (mps + F);
               if (sec1 <= sec2)
                 {
                   global_sec += sec1;
                   break;
                   own += sec1 * mps;
                 }
               else
                 {
                   mps += F;
                   global_sec += med / mps;
                 }
             }
           else 
             {
               sec1 = med / mps;
               global_sec += sec1;
               own += sec1 * mps;
             }
           //printf (" %lf %lf %lf %lf\n", X, own, med, global_sec);
         }
         
       fprintf (fout, "%.7lf", global_sec);
       
       if (i != tests - 1) fprintf (fout, "\n");
     }

  fclose (fin);
  fclose (fout);
  
  return 0;
}
