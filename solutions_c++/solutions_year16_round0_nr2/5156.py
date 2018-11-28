#include <iostream>
#include <cstdio>

void solve()
{
  char str[101];
  scanf("%s", str);
  int len = strlen(str);
  bool plus = true;
  int cnt = 0;
  for(int i = len - 1; i>=0; i--)
  {
    if(str[i] == '+')
    {
      if (!plus)
        cnt++;
      plus = true;
    }
    else
    {
      if (plus)
        cnt++;
      plus = false;
    }
  }
  printf("%d\n", cnt);
}

int main()
{
  freopen("BLin.txt", "r", stdin);
  freopen("BLout.txt", "w", stdout);
  
  int tc;
  scanf("%d", &tc);
  for(int i=1; i<=tc; i++)
  {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}
