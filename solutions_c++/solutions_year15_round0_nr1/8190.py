#include <stdio.h>
char s[1010];
long long n, a, i, j, cnt, stand, come;

int main(void)
{
  freopen("A-large.in", "r", stdin);
  freopen("sol.out", "w", stdout);
  scanf("%lld", &n);
  for(i = 1; i <= n; i++)
  {
    cnt = stand = come = 0; 
    scanf("%lld %s",&a, &s);
    for(j = 0; j <= a; j++)
    {
      if(s[j] != '0')
        {
		  if(stand >= j) stand += s[j] - 48; else
          {
			  come = j - stand; 
			  cnt += come; 
			  stand += (s[j] - 48) + come;
		  }
	    }
    }
    printf("Case #%lld: %lld\n", i, cnt);
  }
  return 0;
}
