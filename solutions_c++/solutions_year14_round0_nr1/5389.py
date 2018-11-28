#include<stdio.h>

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w", stdout);
	int num[17];
	int T, R, row[4];
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++)
	{
		for(int i=1;i<=16;i++)
			num[i]=0;
		scanf("%d",&R);
		for(int i=1;i<=4;i++)
		{
			for(int j=0;j<4;j++)
				scanf("%d",&row[j]);
			if(i==R)
			{
				for(int j=0;j<4;j++)
					num[row[j]]++;
			}
		}
		scanf("%d",&R);
		for(int i=1;i<=4;i++)
		{
			for(int j=0;j<4;j++)
				scanf("%d",&row[j]);
			if(i==R)
			{
				for(int j=0;j<4;j++)
					num[row[j]]++;
			}
		}
		int res, rescount = 0;
		for(int i=1;i<=16;i++)
		{
			if(num[i]>1)
			{
				++rescount;
				res = i;
			}
		}
		if(rescount==1)
			printf("Case #%d: %d\n",cs, res);
		else if(rescount > 1)
			printf("Case #%d: Bad magician!\n", cs);
		else if(rescount < 1)
			printf("Case #%d: Volunteer cheated!\n", cs);
	}

	return 0;
}