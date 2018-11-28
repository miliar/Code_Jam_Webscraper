#include <cstdio>
#include <algorithm>
using namespace std;

double naomi[1001], ken[1001];
int main()
{
    int tcase;
    scanf ("%d", &tcase);
    for (int i = 1 ; i <= tcase; i ++)
    {
          int N;
          scanf ("%d", &N);
          
          for (int k = 0 ; k < N; k ++)
              scanf ("%lf", &naomi[k]);

          for (int k = 0 ; k < N; k ++)
              scanf ("%lf", &ken[k]);
              
          sort (naomi, naomi + N);
          sort (ken, ken + N);
          
          /* deceitful war */
          int n = 0, k = 0, n_deceive_win = 0;
          while (n < N && k < N)
          {
                if (naomi[n] > ken[k])
                {
                   n_deceive_win ++;
                   n ++ ;
                   k ++ ;
                }
                else n ++;
          }
          
          /* war */
          int n_win = 0;
          n = 0; k = 0;
          while (n < N && k < N)
          {
                if (naomi[n] < ken[k])
                {
                   n ++ ;
                   k ++ ;
                }
                else
                {
                    k ++;
                    n_win ++;
                }
          }
          
          printf ("Case #%d: %d %d\n", i, n_deceive_win, n_win);
    }
    return 0;
}
