#include<stdio.h>
int main()
{
	int loop,l;
	scanf("%d",&loop);
	for(l=1;l<=loop;l++)
	{
		int a[4][4];
		int b[4][4];
		int ansa;
		int ansb;
		int i,j,k;
		int answer;
		int count=0;
		scanf("%d",&ansa);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&ansb);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&b[i][j]);
			}
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[ansa-1][j]==b[ansb-1][i])
				{
					
					count++;
					answer=a[ansa-1][j];
				}
			}
		}
		if(count==0)
		{
			printf("Case #%d: Volunteer cheated!\n",l);
		}
		else if(count==1)
		{
			printf("Case #%d: %d\n",l,answer);
		}
		else
		{
			printf("Case #%d: Bad magician!\n",l);
		}
	}
	return 0;
}
