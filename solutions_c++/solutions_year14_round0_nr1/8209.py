#include<stdio.h>
#include<stdlib.h>

using namespace std;
int main()
{
  int T, i, j, k, t;
  int ans1, ans2, ar1[5][5], ar2[5][5];
  scanf("%d", &T);
  for(t=1;t<=T;t++)
    {
      int flag[17] = {0}, count_viable;
      scanf("%d", &ans1);
      for(i=1;i<=4;i++)
	for(j=1;j<=4;j++)
	  scanf("%d", &ar1[i][j]);
      for(j=1;j<=4;j++)
	flag[ar1[ans1][j]] = 1;
      scanf("%d", &ans2);
      for(i=1;i<=4;i++)
	for(j=1;j<=4;j++)
	  scanf("%d", &ar2[i][j]);
      for(j=1;j<=4;j++)
	flag[ar2[ans2][j]] += 1;
      for(count_viable=0, k=1;k<=16;k++, count_viable += (flag[k] == 2));
      printf("Case #%d: ", t);
      if(count_viable == 1)
	{
	  for(k=1;flag[k]!=2;k++);
	  printf("%d\n", k);
	}
      else if(count_viable == 0)
	printf("Volunteer cheated!\n");
      else if(count_viable > 1)
	printf("Bad magician!\n");
    }
}
