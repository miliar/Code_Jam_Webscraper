#include<stdio.h>

int main()
{
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  int t, smax, n, i, j;
  scanf("%d", &t);
  for(i=1; i<=t; i++)
  {
    long unsigned count=0, ans=0;
    char s[1002]={0};
    scanf("%d %s", &smax, s);
    for(j=0; j<=smax; j++)
    {
      n=s[j]-'0';
      if(count<j && n)
      {
	ans+=(j-count);
	count+=(j-count);
      }
      count+=n;
    }
    printf("Case #%d: %lu\n", i, ans);
  }
  return 0;
}