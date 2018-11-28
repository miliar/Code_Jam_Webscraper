#include <stdio.h>
#include <string.h>
int arrange1[4][4],arrange2[4][4];
int main(void)
{
	int t,ans1,ans2;
	int count[20];
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		memset(count,0,sizeof(count));
		scanf("%d",&ans1);
		for(int i=0;i<4;i++)for(int j=0;j<4;j++)scanf("%d",&arrange1[i][j]);
		scanf("%d",&ans2);
		for(int i=0;i<4;i++)for(int j=0;j<4;j++)scanf("%d",&arrange2[i][j]);
		for(int i=0;i<4;i++)
		{
			//printf("%d %d\n",arrange1[ans1][i],arrange2[ans2][i]);
			count[arrange1[ans1-1][i]]++;
			count[arrange2[ans2-1][i]]++;
		}
		int ans=0;
		bool m=0;
		//for(int i=1;i<=16;i++)printf("%d ",count[i]);
		for(int i=1;i<=16;i++)if(count[i]==2)
		{
			if(ans)m=1;else ans=i;
		}
		if(m)printf("Case #%d: Bad magician!\n",k);
		else if(ans)printf("Case #%d: %d\n",k,ans);
		else printf("Case #%d: Volunteer cheated!\n",k);
	}
	return 0;
}