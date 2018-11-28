#include<stdio.h>
#include<string.h>

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t, a, b, i, j, mark[20], grid[4][4];
	scanf("%d",&t);
	for(int cs = 0; cs< t; cs++)
	{
		scanf("%d",&a);a--;
		for(i=1;i<=16;i++)
			mark[i] = 0;

		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&grid[i][j]);

		for(j=0;j<4;j++)
			mark[grid[a][j]]++;
		
		scanf("%d",&b);b--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&grid[i][j]);

		int cnt = 0, ans;
		for(j=0;j<4;j++)
		{
			mark[grid[b][j]]++;
			if(mark[grid[b][j]] == 2)
				cnt++, ans = grid[b][j];
		}

		if(cnt==0)
			printf("Case #%d: Volunteer cheated!\n",cs+1);
		else if(cnt==1)
			printf("Case #%d: %d\n",cs+1,ans);
		else
			printf("Case #%d: Bad magician!\n",cs+1);
	}
	return 0;
}