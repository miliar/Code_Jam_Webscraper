#include<stdio.h>
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t,ans,cand;
	int boar[4][4];
	bool exist[16],hit;
	scanf("%d",&t);
	for(int c=0;c<t;c++)
	{
		hit=false;
		for(int b=0;b<16;b++)
			exist[b]=false;
		scanf("%d",&ans);
		ans--;
		for(int b=0;b<4;b++)
			for(int k=0;k<4;k++)
				scanf("%d",&boar[b][k]);
		for(int b=0;b<4;b++)
			exist[(boar[ans][b]-1)]=true;
		scanf("%d",&ans);
		ans--;
		for(int b=0;b<4;b++)
			for(int k=0;k<4;k++)
				scanf("%d",&boar[b][k]);
		for(int b=0;b<4;b++)
		{
			if(exist[(boar[ans][b]-1)])
			{
				if(!hit)
				{
					cand=boar[ans][b];
					hit=true;
				}
				else
				{
					printf("Case #%d: Bad magician!\n",c+1);
					break;
				}
			}
			if(b==3)
			{
				if(!hit)
					printf("Case #%d: Volunteer cheated!\n",c+1);
				else
					printf("Case #%d: %d\n",c+1,cand);
			}
		}
	}
	return 0;
}