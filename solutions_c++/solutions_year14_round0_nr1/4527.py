#include <cstdio>

using namespace std;
#define MAX_N 17
#define CHEAT 0
#define BAD -1

int seem[MAX_N];

int main()
{
  int row,ans,T;
  scanf(" %d",&T);
  for(int t = 1; t <= T;t++)
    {
      for(int i = 0; i < MAX_N;i++)
	seem[i] = 0;
      for(int k = 0; k < 2;k++)
	{
	  scanf("%d",&row);
	  for(int i = 1; i <= 4;i++)
	    for(int j = 1; j <= 4;j++)
	      {
		int inp;
		scanf(" %d",&inp);
		if(i == row)
		  seem[inp]++;
	      }
	}
      ans = CHEAT;
      for(int i = 1; i <= 16;i++)
	{
	  if(seem[i] == 2)
	    {
	      if(ans == CHEAT)
		ans = i;
	      else
		ans = BAD;
	    }
	}
      printf("Case #%d: ",t);
      if(ans >= 1)
	printf("%d\n",ans);
      else if( ans == BAD)
	printf("Bad magician!\n");
      else
	printf("Volunteer cheated!\n");
    }
  return 0;
}
