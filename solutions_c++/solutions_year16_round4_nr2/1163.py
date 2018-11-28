#include <cassert>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <vector>
#include <list>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

typedef unsigned long long ull_t;

int main ()
{
  freopen ("in.txt", "rb", stdin);
  freopen ("out.txt", "wb", stdout);

  int T;
  scanf ("%d", &T);
  for (int t = 1; t <= T; t++)
  {
    printf ("Case #%d: ", t);

    int N, K;
    scanf ("%d %d", &N, &K);

    vector<double> P;
    for (int i = 0; i < N; i++)
    {
      double q = 0;
      scanf ("%lf", &q);

      P.push_back (q);
    }

    sort (P.begin (), P.end());

    double answer = 0.0;

    {
      for (int i = 0; i < (1 << N); i++)
      {
        vector<double> Pl;

        int Pl_size = 0;
        for (int j = 0; j < N; j++)
        {
          if (i & (1 << j))
          {
            Pl_size++;
          }
        }

        if (Pl_size != K)
        {
          continue;
        }

        for (int j = 0; j < N; j++)
        {
          if (i & (1 << j))
          {
            Pl.push_back (P[j]);
          }
        }

        double answer_local = 0.0;

        for (int j = 0; j < (1 << Pl.size ()); j++)
        {
          int cnt = 0;

          for (int q = 0; q < Pl.size (); q++)
          {
            if (j & (1 << q))
            {
              cnt++;
            }
          }

          if (2 * cnt == Pl.size ())
          {
            double pcalc = 1.0;

            for (int q = 0; q < Pl.size (); q++)
            {
              if (j & (1 << q))
              {
                pcalc *= Pl[q];
              }
              else
              {
                pcalc *= (1 - Pl[q]);
              }
            }

            answer_local += pcalc;
          }
        }

        if (answer_local > answer)
        {
          answer = answer_local;
        }
      }
    }

    printf ("%0.10lf\n", answer);

    fflush (stdout);
  }

  fclose (stdin);
  fclose (stdout);

  return 0;
}
