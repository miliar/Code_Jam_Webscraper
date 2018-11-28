#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int s[10000];

int main()
{
  int nb_cas;
  scanf("%d",&nb_cas);
  for(int cas = 1; cas <= nb_cas; cas++)
    {
      printf("Case #%d: ",cas);
      int n,x;
      scanf("%d%d",&n,&x);
      for(int i = 0; i < n; i++)
	scanf("%d",&s[i]);
      int a = 0;
      int b = n-1;
      sort(s,s+n);
      int y = n;
      while(a<b)
	{
	  //	  printf("%d %d\n",a,b);
	  if(s[a]+s[b]<=x)
	    {
	      y--;
	      a++;
	      b--;
	    }
	  else
	    b--;
	}
      printf("%d\n",y);
    }
  return 0;
}
