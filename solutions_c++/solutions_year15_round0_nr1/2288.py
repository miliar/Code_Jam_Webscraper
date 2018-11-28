#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("A-large.in", "r"), * fout = fopen ("alargeout.txt", "w");

void work (int r)
{
     fprintf (fout, "Case #%d: ", r);
     
     int s;
     fscanf (fin, "%d", &s);
     //printf ("\n%d", s);
     int num[1001];
     int stand = 0;
     int ans = 0;
     for (int i = 0; i < s + 1; i ++)
     {
         char c;
         fscanf (fin, "%c", &c);
         if (c == ' ') fscanf (fin, "%c", &c);
         num[i] = c - '0';
         //printf ("%d ", num[i]);
         if (i == 0)
               stand = num[0];
         if (i > 0)
         {
               if (stand < i)
               {
                  ans += i - stand;
                  stand = i + num[i];
               }
               else
                   stand = stand + num[i];
         }
     }     
     fprintf (fout, "%d\n", ans);
     return;
}

int main ()
{
    int T = 0;
    fscanf (fin, "%d", &T);
    for (int i = 0; i < T; i ++)
    {
        work (i + 1);
    }
    return 0;
}
