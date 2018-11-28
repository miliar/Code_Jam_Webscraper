#include <stdio.h>
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int ans,cnt=0,mark[1+16]={0};
		for(int i=0;i<2;i++)
		{
			int num;
			scanf("%d",&num);
			for(int row=1;row<=4;row++)
				for(int col=1;col<=4;col++)
				{
					int card;
					scanf("%d",&card);
					if(row==num)
						mark[card]++;
				}
		}
		for(int i=1;i<=16;i++)
			if(mark[i]==2)
			{
				ans=i;
				cnt++;
			}
		printf("Case #%d: ",t);
		if(cnt==0)
			printf("Volunteer cheated!");
		else if(cnt==1)
			printf("%d",ans);
		else
			printf("Bad magician!");
		printf("\n");
	}
	return 0;
}
