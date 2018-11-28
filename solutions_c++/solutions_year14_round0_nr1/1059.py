#include <cstdio>
#include <bitset>

using namespace std;

int main()
{
  int tcase;
  scanf("%d",&tcase);
  bitset<32> app;
  for(int tnum = 1; tnum <= tcase; tnum++)
    {
      app.reset();
      const int n = 4;
      int r;
      scanf("%d",&r);
      for(int i = 0; i < n; i++)
	for(int j = 0; j < n; j++)
	  {
	    int v;
	    scanf("%d",&v);
	    if (i == r - 1) app[v] = true;
	  }

      int tot = 0,res;
      scanf("%d",&r);
      for(int i = 0; i < n; i++)
	for(int j = 0; j < n; j++)
	  {
	    int v;
	    scanf("%d",&v);
	    if (i == r - 1 && app[v]) ++tot,res = v;
	  }

      printf("Case #%d: ",tnum);
      if (tot == 0) puts("Volunteer cheated!");
      else if (tot == 1) printf("%d\n",res);
      else puts("Bad magician!");
    }
  return 0;
}
