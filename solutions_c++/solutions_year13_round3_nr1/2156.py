
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


char str[200];
int sum[200];
int n;

bool check(char c)
{
  if(c!='a'&&c!='e'&&c!='i'&&c!='o'&&c!='u')
    return true;
  return false;
}
void solve()
{
  int len = strlen(str);
  int ans = 0;
  for(int i=0;i<len;i++)
    {
      int cnt=0;
      for(int j=i;j<len;j++)
	{
	  if(check(str[j]))
	    cnt++;
	  else
	    cnt =0;
	  if(cnt==n)
	    {
	      ans += len-j;
	      break;
	    }
	}
    }
  printf("%d\n",ans);
}

int main()
{  
  int T,ncase=1;
  scanf("%d",&T);
  while(ncase<=T)
    {
      scanf("%s%d",str,&n);
      printf("Case #%d: ",ncase++);
      solve();
    }
  return 0;
}
