#include <stdio.h>

int ra,rb;
int a[5][5],b[5][5];

int main()
{
	int T;
	int ca = 1;
	int i,j;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&ra);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&rb);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				scanf("%d",&b[i][j]);
			}
		}
		int cnt = 0,ans = 0;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if( a[ra][i] == b[rb][j] )
				{
					cnt++;
					ans = a[ra][i];
				}
			}
		}
		switch(cnt)
		{
			case 1:
				printf("Case #%d: %d\n",ca++,ans);
				break;
			case 0:
				printf("Case #%d: Volunteer cheated!\n",ca++);
				break;
			default:
				printf("Case #%d: Bad magician!\n",ca++);
				break;
		}
	}
	return 0;
}

