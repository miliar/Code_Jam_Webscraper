#include <iostream>
#include <cstdio>
#include <functional>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int t;
int n;
int a[1005];
int main()
{
  cin >> t;
  int cur = 1;
  while(cur <= t)
  {
    cin >> n;
    cin >> a[0];
    int best = a[0];
    for(int i = 1; i < n; i++)
    {
      cin >> a[i];
      best = max(best, a[i]);
    }
    for(int i = 1; i <= 1000; i++)
    {
      int sp = 0;
      for(int j = 0; j < n; j++)
      {
        if(a[j] > i)
        {
          if(a[j] % i != 0)
            sp += a[j]/i;
          else
            sp += a[j]/i-1;
        }
      }
      best = min(best, sp + i);
    }
    printf("Case #%d: %d\n", cur, best);
    cur++;
  }
}
