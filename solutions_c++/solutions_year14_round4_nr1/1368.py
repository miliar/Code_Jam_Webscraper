#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int a[12345];
              
int main (void)
{
  int test, tests;
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int i, j, res = 0, n, c;
    scanf ("%d %d", &n, &c);
    for (i = 0; i < n; i++)
      scanf ("%d", &a[i]);
    sort (a, a + n);
    i = 0;
    j = n-1;
    res = n;

    while (i < j)
    {
      while (i < j && a[i] + a[j] > c)
        j--;
      if (i < j)
        res--;
      i++;
      j--;
   }   
     
    printf ("Case #%d: %d\n", test + 1, res);

  }
  return 0;
}
