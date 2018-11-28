# include<cstdio>
# include<cmath>
# include<algorithm>
using namespace std;
int main()
{
	int i,j,k,t,ans1,ans2,count,ans;
	int a[4][4],b[4][4];
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		count = 0;
		scanf("%d",&ans1);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&ans2);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&b[i][j]);
			}
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[ans1-1][i] == b[ans2-1][j])
				{
					ans = a[ans1-1][i];
					count++;
				}
			}
		}
		if(count==1)
			printf("Case #%d: %d\n",k,ans);
		else
		if(count==0)
			printf("Case #%d: Volunteer cheated!\n",k);
		else
			printf("Case #%d: Bad magician!\n",k);
	}
	return 0;
}