#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int t, i=0, j=0;
	scanf("%d",&t);
	int tt=0;
	while(t--)
	{
		tt++;
		int firstarr[5][5], secondarr[5][5], store, answer1, answer2;
		scanf("%d",&answer1);
		for (i=1; i<=4; i++)
		{
			for (j=1; j<=4; j++)
			{
				scanf("%d",&firstarr[i][j]);
			}
		}

		scanf("%d",&answer2);
		for (i=1; i<=4; i++)
		{
			for (j=1; j<=4; j++)
			{
				scanf("%d",&secondarr[i][j]);
			}
		}
		int flag = 0;
		for(i=1; i<=4; i++)
		{
			for (j=1; j<=4; j++)
			{
				if(firstarr[answer1][j]==secondarr[answer2][i])
				{
					flag++;
					store = firstarr[answer1][j];
					if(flag>1)
						break;
				}
			}
			if(flag>1)
				break;
		}
		
		switch(flag)
		{
			case 1: printf("Case #%d: %d\n", tt, store);
					break;

			case 0: printf("Case #%d: Volunteer cheated!\n", tt);
					break;
					
			default: printf("Case #%d: Bad magician!\n", tt);
					break;
		}

	}
	return 0;
}
