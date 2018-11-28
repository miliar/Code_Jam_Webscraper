#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>

using namespace std;

bool check(char c)
{
  return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
}

char s[1000100];

int main()
{
  int tn;
  scanf("%d",&tn);
  for(int t = 1; t <= tn; t++)
    {
      scanf("%s",s);
      int len = strlen(s);
      int prep = -1;
      
      int m;
      scanf("%d",&m);
      long long ans = 0;
      for(int i = 0,j; i < len; )
	if (check(s[i]))
	{
	  for(j = i + 1; j < len && check(s[j]); j++);
	  //printf("%d %d\n",i,j);
	  
	  if (j - i >= m)
	    {
	      ans += (long long)(i - prep) * (len - (i + m) + 1);
	      for(int k = i + 1; k + m <= j; k++)
		ans += (len - (k + m) + 1);
	      prep = j - m;
	    }

	  i = j;
	}
	else i++;

      cout << "Case #" << t << ": " << ans << endl;
    }
  return 0;
}
