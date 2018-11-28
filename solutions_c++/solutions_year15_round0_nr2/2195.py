#include <cstdio>
#include <climits>
#include <cstring>
#include <algorithm>
using namespace std;

int input[1001];

bool isok(int D, int time_max)
{
  for(int high = 1; high <= time_max; ++high)
  {
    int extra = 0;
    bool isok = true;
    for(int i = 0; i < D; ++i)
    {
      if(input[i] <= high)
        continue;
      if(input[i] % high == 0)
        extra += input[i] / high - 1;
      else
        extra += input[i] / high;
      if(extra + high > time_max)
      {
        isok = false;
        break;
      }
    }
    if(isok)
      return true;
  }
  return false;
}

int main()
{
  int T = 0;
  scanf("%d", &T);
  for(int Case = 1; Case <= T; ++Case)
  {
    int D = 0;
    scanf("%d", &D);
    int tmax = 0;
    for(int i = 0; i < D; ++i)
    {
      scanf("%d", input + i);
      tmax = max(tmax, input[i]);
    }
    int ans = 0;
    {
      int l = 1, r = tmax;
      while(r - l > 1)
      {
        int mid = (r + l) >> 1;
        if(isok(D, mid))
          r = mid;
        else
          l = mid;
      }
      if(isok(D, l))
        ans = l;
      else
        ans = r;
    }
    printf("Case #%d: %d\n", Case, ans);
  }
  return 0;
}
