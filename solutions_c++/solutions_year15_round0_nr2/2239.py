#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("B-large.in", "r"), * fout = fopen ("bsmall.out", "w");

int num[1000];

void work (int r)
{
     fprintf (fout, "Case #%d: ", r);
     int D;
     fscanf (fin, "%d", &D);
     int maxi = 0;
     for (int i = 0; i < D; i ++)
     {
         int P;
         fscanf (fin, "%d", &P);
         if (P > maxi) maxi = P;
         num [P - 1] ++;
     }
     int re = maxi;
     for (int k = 1; k < maxi; k ++)
     {
         int tmp = 0;
         for (int l = 0; l < maxi; l ++)
         {
             int cou = (l + 1) / k;
             if (((l + 1) % k) == 0) cou --;
             tmp += cou * num[l];
         }
         if (tmp + k < re) re = tmp + k;
     }
     fprintf (fout, "%d\n", re);
     return;
}

int main ()
{
    int T = 0;
    fscanf (fin, "%d", &T);
    for (int i = 0; i < T; i ++)
    {
        //printf ("%d ", i);
        for (int j = 0; j < 1000; j ++)
        {
            num[j] = 0;
        }
        work (i + 1);
    }
    return 0;
}