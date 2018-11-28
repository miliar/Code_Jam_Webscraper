#include<stdio.h>
int main()
{
	int T;
	int row;
	int cards[4][4];
	int temp[4];
	int n;
	int i,j;
	int count;
	int card;
	scanf("%d",&T);
	for(n=0;n<T;n++)
	{
		count=0;
		scanf("%d",&row);
		for(i=0;i<4;i++)
		{
			scanf("%d %d %d %d",cards[i],cards[i]+1,cards[i]+2,cards[i]+3);
		}
		for(i=0;i<4;i++)
		{
			temp[i]=cards[row-1][i];
		}
		scanf("%d",&row);
		for(i=0;i<4;i++)
		{
			scanf("%d %d %d %d",cards[i],cards[i]+1,cards[i]+2,cards[i]+3);
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(temp[i]==cards[row-1][j])
				{
					count++;
					card=temp[i];
				}
			}
			if(count>1)
			{
				break;
			}
		}
		printf("Case #%d: ",n+1);
		switch(count)
		{
		case 0:
			puts("Volunteer cheated!");
			break;
		case 1:
			printf("%d\n",card);
			break;
		default:
			puts("Bad magician!");
		}
	}
	return 0;
}