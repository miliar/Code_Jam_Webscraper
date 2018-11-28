#include <iostream>
#include <cstdio>
#include <memory.h>

using namespace std;

long long n;

void solve()
{
  scanf("%lld", &n);
  if (n == 0)
  {
    printf("INSOMNIA\n");
    return;
  }

  bool used[10];
  memset(used, 0x00, sizeof used);

  int i, j;
  for(i=1;;i++)
  {
    long long k = i*n;
    while(k > 0)
    {
      used[k%10] = true;
      k/=10;
    } 

    for(j=0;j<10;j++)
      if(!used[j])
        break;

    if(j == 10)
      break;
  }
  printf("%lld\n", i*n);
}

int main()
{
  freopen("ALin.txt", "r", stdin);
  freopen("ALout.txt", "w", stdout);

  int tc;
  scanf("%d", &tc);
  for(int i=1; i<=tc; i++)
  {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}
