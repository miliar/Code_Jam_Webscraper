#include <bits/stdc++.h>

int main()
{
  char s[101];
  int t, ans = 0, ls, j, cas = 0;
  scanf("%d", &t);
  while(t--)
  {
    scanf(" %s", s);
    ls = strlen(s);
    ans = 0;
    j = -1;
    for(int i = 0; i < ls; ++i)
    {
      if(s[i] == '+' && j == -1) continue;
      if(s[i] == '+')
      {
        if(j == 0)
         ++ans;
        else
          ans += 2;
        j = -1;
        continue;
      }
      if(j == -1) j = i;
    }
    if(j != -1)
    {
      if(!j)
        ++ans;
      else
        ans += 2;
    }
    printf("Case #%d: %d\n", ++cas, ans);
  }
}
