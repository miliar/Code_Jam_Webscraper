#include <stdio.h>

int main()
{
	int card[20];
	int tc;
	scanf("%d",&tc);
	for(int ct=1;ct<=tc;ct++)
	{
		int ans;
		int ret = 0;
		for(int i=0;i<17;i++)
			card[i] = 0;
		scanf("%d", &ans);
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				if(i==ans-1)
				{
					int tmp;
					scanf("%d", &tmp);
					card[tmp]++;
				}
				else
					scanf("%*d");
		scanf("%d", &ans);
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				if(i==ans-1)
				{
					int tmp;
					scanf("%d", &tmp);
					card[tmp]++;
					if(card[tmp]==2)
					{
						if(ret == 0)
							ret = tmp;
						else
							ret = -1;
					}
				}
				else
					scanf("%*d");
		printf("Case #%d: ", ct);
		if(ret == -1)
			puts("Bad magician!");
		else if(ret == 0)
			puts("Volunteer cheated!");
		else
			printf("%d\n",ret);
	}
	return 0;
}
