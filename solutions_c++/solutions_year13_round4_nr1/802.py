#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>

#define F first
#define S second

using namespace std;

const int MaxM = 1234, Mod = 1000002013;

vector <pair <long long, long long> > l;
vector <pair <long long, long long> > r;

int main (void)
{
  int test, tests;

  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int i, j, n, m;
    long long o, e, p;
    long long res = 0, sum = 0;
    scanf ("%d %d", &n, &m);
    l.clear();
    r.clear();
    l.resize (m);
    r.resize (m);
    for (i = 0; i < m; i++)
    {
      scanf ("%I64d %I64d %I64d", &o, &e, &p);
      sum += (((e - o) * (e - o - 1) / 2 + (e - o) * (n - e + o + 1)) % Mod) * p;
      sum %= Mod;
      l[i] = make_pair (o, p);
      r[i] = make_pair (e, p);
    }
    sort (l.begin(), l.end());
    sort (r.begin(), r.end());
    res = 0;
    for (i = 0; i < m; i++)
    {
      for (j = m-1; j >= 0; j--)
        if (r[i].F >= l[j].F)
        {
          p = min (r[i].S, l[j].S);
          r[i].S -= p;
          l[j].S -= p;
          e = r[i].F;
          o = l[j].F;
          res += (((e - o) * (e - o - 1) / 2 + (e - o) * (n - e + o + 1)) % Mod) * p;
          res %= Mod;
        }
    }
    res = sum - res;
    while (res < 0)
      res += Mod;
    while (res >= Mod)
      res -= Mod;

    printf ("Case #%d: %I64d\n", test + 1, res);
      
    
  }
  return 0;
}
