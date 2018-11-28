#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int nbcas;

int main()
{
  scanf("%d",&nbcas);
  for(int cas = 1; cas <= nbcas; cas++)
    {
      int a[2];
      bool t[16];
      for(int i=0;i<16;i++) t[i] = true;
      for(int grid = 0; grid < 2; grid++)
	{
	  int row;
	  scanf("%d",&row);
	  for(int i = 1; i <= 4; i++)
	    for(int j = 0; j < 4; j++)
	      {
		int k;
		scanf("%d",&k);
		if(i != row) t[k-1]=false;
	      }
	}
      int n_ok = 0;
      int hidden = 0;
      for(int i = 0; i < 16; i++)
	if(t[i]) 
	  {
	    hidden = i+1;
	    n_ok++;
	  }
      printf("Case #%d: ",cas);
      if(n_ok == 0)
	printf("Volunteer cheated!\n");
      else if(n_ok == 1)
	printf("%d\n",hidden);
      else
	printf("Bad magician!\n");
    }
  return 0;
}
