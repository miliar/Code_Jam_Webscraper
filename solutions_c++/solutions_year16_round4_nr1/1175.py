#include <cassert>
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

    int N, R, P, S;
    scanf ("%d %d %d %d", &N, &R, &P, &S);

    int NN = (1 << N);

    while (R + P + S != 1
           && P >= 0 && R >= 0 && S >= 0)
    {
      int Pn = (P + R - S) / 2;
      int Rn = (R + S - P) / 2;
      int Sn = (P + S - R) / 2;

      P = Pn; R = Rn; S = Sn;
    }

    if (P < 0 || R < 0 || S < 0)
    {
      printf ("IMPOSSIBLE\n");
    }
    else
    {
      vector<char> str;

      if (P == 1) str.push_back ('P');
      else if (R == 1) str.push_back ('R');
      else str.push_back ('S');

      while (str.size () != NN)
      {
        vector<char> str2;

        for (int i = 0; i < str.size (); i++)
        {
          if (str [i] == 'P')
          {
            str2.push_back ('P');
            str2.push_back ('R');
          }
          else if (str [i] == 'R')
          {
            str2.push_back ('R');
            str2.push_back ('S');
          }
          else
          {
            str2.push_back ('P');
            str2.push_back ('S');
          }
        }

        str = str2;
      }

      vector<string> s;

      for (int i = 0; i < str.size (); i++)
      {
        s.push_back (string (1, str[i]));
      }

      while (s.size () != 1)
      {
        vector<string> s2;

        for (int i = 0; i < s.size(); i += 2)
        {
          if (s[i] < s[i + 1])
          {
            s2.push_back (s[i] + s[i + 1]);
          }
          else
          {
            s2.push_back (s[i + 1] + s[i]);
          }
        }

        s = s2;
      }

      printf ("%s\n", s[0].c_str());
    }

    fflush (stdout);
  }

  fclose (stdin);
  fclose (stdout);

  return 0;
}
