#include <cstdlib>
#include <cstdio>

FILE * fin = fopen ("D-small-attempt0.in", "r"), *fout = fopen ("dsmall.out", "w");

void work (int round)
{
     fprintf (fout, "Case #%d: ", round);
     int x, r, c;
     fscanf (fin, "%d%d%d", &x, &r, &c);
     if ((r * c) % x != 0 || x >= 7)
     {
        fprintf (fout, "RICHARD\n");
        return;
     }
     if ((r >= x) && (c >= x) || (x == 2))
     {
           fprintf (fout, "GABRIEL\n");
           return;
     }
     if ((r < (x + 1)/2) || (c < (x + 1)/2)|| r*c == x)
     {
              fprintf (fout, "RICHARD\n");
              return;
     }
     if (x == 3)
     {
           fprintf (fout, "GABRIEL\n");
           return;
     }
     if (x == 4)
     {
           if (r == 2 || c == 2)
              fprintf (fout, "RICHARD\n");
           else fprintf (fout, "GABRIEL\n");
           return;
     }
     if (x == 5)
     {
           fprintf (fout, "GABRIEL\n");
           return;
     }
     if (x == 6)
     {
           if ((r == 3) || (c == 3))
           {
                  fprintf (fout, "RICHARD\n");
                  return;
           }
           fprintf (fout, "GABRIEL\n");
           return;
     }
     return;
}

int main ()
{
    int T;
    fscanf (fin, "%d", &T);
    for (int i = 0; i < T; i ++)
    {
        work (i + 1);
    }
    return 0;
}