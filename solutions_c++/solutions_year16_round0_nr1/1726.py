
#include <iostream>
using namespace std;

long long solve(int n)
{
  if( n == 0 )
  {
    return -1;
  }

  int mask = 0;
  int finalMask = (1<<10) - 1;
  long long i;
  for(i = 1; mask != finalMask; i++)
  {
    long long temp = i*n;
    while(temp)
    {
      mask |= 1 << (temp % 10);
      temp /= 10;
    }
  }

  return i - 1;
}

void solve()
{
  int n;
  scanf("%d", &n);
  int res = solve(n);

  if(res == -1)
  {
    printf("%s\n", "INSOMNIA");
  }
  else
  {
    printf("%lld\n", (long long) res * n);
  }
}
int main()
{
  // long long mx = 0;
  // for(int i = 0; i <= 1000000 ; i ++)
  // {
  //   mx = max(mx, (long long) solve(i) * i);
  // }
  // cout << mx << endl;
  // return 0;
  int t;
  scanf("%d", &t);

  for(int i = 1; i <= t; i++)
  {
    printf("Case #%d: ", i);
    solve();
  }

}
