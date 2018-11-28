#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

char s[128];

int main()
{
  int n,m;
  scanf ("%d",&n);
  for (int i = 1; i <= n; i++)
    {
      scanf ("%s",s);
      m = strlen(s);
      int ans = 0, flag = 0;
      for (int j = m-1; j >= 0; j--)
	{
	  if (s[j] == '-')
	    {
	      if ((j == m-1) || (s[j+1] == '+')) ans++;
	      flag = 1;
	    }
	  else if (flag && (s[j+1] == '-')) ans++;
	}
      printf ("Case #%d: %d\n",i,ans);
    }
}
