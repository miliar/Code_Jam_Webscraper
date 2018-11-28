#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;

int T;

int n;
int a[1000];
int c[1000];

int x;

int f(int d, int e, int &p)
{
  int r = 0;
  while (d <= e)
  {
    ++r;
    d += d - 1;
  }
  p = d;
  return r;
}

int main()
{
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    scanf("%d %d", &x, &n);
    for (int i = 0; i < n; ++i)
      scanf("%d", &a[i]);
    sort(a, a + n);
    int res = 0;

    if (x == 1)
    {
      res = n;
    }
    else
    {
    for (int i = 0; i < n; ++i)
    {
      if (a[i] < x)
      {
        x += a[i];
      }
      else
      {
        
          int p;
          int q = f(x, a[i], p);
          if ( q < n - i )
          {
            x = p;
            x += a[i];
            res += q;
          }
          else
            res += 1;
        
      }   
    }
    }
    printf("Case #%d: %d\n", t+1, res);
  }
  return 0;
}