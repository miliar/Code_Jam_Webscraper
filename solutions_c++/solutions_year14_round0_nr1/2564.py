#include<cstdio>
using namespace std;
int main()
{
	freopen("F:\\A-small-attempt0.in","r",stdin);
	freopen("F:\\A-small.out","w",stdout);
	int T(0);
	int ans1(0),ans2(0);
	int card[2][4][4];
	int count=0;
	int res=0;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		count=0;
		scanf("%d",&ans1);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&card[0][i][j]);
		scanf("%d",&ans2);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&card[1][i][j]);
		ans1--;
		ans2--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(card[0][ans1][i]==card[1][ans2][j])
				{
					res=card[0][ans1][i];
					count++;
				}
			}
		}
		if(!count)
			printf("Case #%d: Volunteer cheated!\n",t);
		else if(count==1)
			printf("Case #%d: %d\n",t,res);
		else
			printf("Case #%d: Bad magician!\n",t);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
