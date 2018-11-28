#include<stdio.h>
#include<string.h>

int main()
{
	int Cards[16];
	int Cards1[17];
	int T,count,R,lim,indx;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		count=0;
		scanf("%d",&R);
		for(int j=0;j<16;j++)
		{
			scanf("%d",&Cards[j]);
		}
		memset(Cards1,0,17*sizeof(int));
		lim = R<<2;
		for(int j=lim-4;j<lim;j++)
		{
			Cards1[Cards[j]] = 1;
		}

		scanf("%d",&R);
		for(int j=0;j<16;j++)
		{
			scanf("%d",&Cards[j]);
		}
		lim = R<<2;
		for(int j=lim-4;j<lim;j++)
		{
			if(Cards1[Cards[j]]==1)
			{
				indx = Cards[j];
				count++;
			}
		}
		
		if(count==1)
		{
			printf("Case #%d: %d\n",i,indx);
		}
		else if(count > 1)
		{
			printf("Case #%d: Bad magician!\n",i);
		}
		else
		{
			printf("Case #%d: Volunteer cheated!\n",i);
		}

	}
	return 0;
}
