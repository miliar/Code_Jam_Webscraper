#include <cstdio>

int a[6][6];
int b[6][6];

int main()
{
  int T,i,x,y,j,o,k,ans;
  scanf("%d",&T);
  for (o=1;o<=T;o++)
  {
    scanf("%d",&x);
    for (i=1;i<=4;i++)
      for (j=1;j<=4;j++)
	scanf("%d",&a[i][j]);
    scanf("%d",&y);
    for (i=1;i<=4;i++)
      for (j=1;j<=4;j++)
	scanf("%d",&b[i][j]);
    i=0;
    for (j=1;j<=4;j++)
      for (k=1;k<=4;k++)
	if (a[x][j]==b[y][k])
	{
	  i++;
	  ans=a[x][j];
	}
    printf("Case #%d: ",o);
    if (i==1)
      printf("%d\n",ans);
    else if (i>1)
      puts("Bad magician!");
    else
      puts("Volunteer cheated!");
  }
  return 0;
}
