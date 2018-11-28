#include<stdio.h>

int main()
{
	freopen("C:\\Users\\Fred\\Downloads\\A-small-attempt0.in","r",stdin);
	freopen("C:\\Users\\Fred\\Downloads\\A-small-attempt0.out","w",stdout);
	int cards1[4][4],cards2[4][4];
	int m,n,t,res;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int res=0;
		int found=0;
		scanf("%d",&m);
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				scanf("%d",&cards1[j][k]);
		scanf("%d",&n);
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				scanf("%d",&cards2[j][k]);
		for(int x=0;x<4;x++)
			for(int y=0;y<4;y++)
			{
				if(cards1[m-1][x]==cards2[n-1][y]&&found==0)
				{
					found=1;
					res=cards1[m-1][x];
				}
				else if(cards1[m-1][x]==cards2[n-1][y]&&found==1)
					found=2;
			}
		if(found==0)
			printf("Case #%d: Volunteer cheated!\n",i);
		else if(found==1)
			printf("Case #%d: %d\n",i,res);
		else
			printf("Case #%d: Bad magician!\n",i);
	}
	return 0;
}