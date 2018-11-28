#include <cstdio>
#include <algorithm>
#include <cstring>
int main()
{
	int t,t1=1;
	scanf("%d",&t);
	while(t1<=t)
	{
		int n;
		scanf("%d",&n);
		int grid[2*n-1][n],i,j,max_value=0;
		for(i=0;i<2*n-1;i++)
		{
			for(j=0;j<n;j++)
			{
				scanf("%d",&grid[i][j]);
				if(grid[i][j]>max_value)
				{
					max_value=grid[i][j];
				}
			}
		}
		//printf(" %d\n",max_value );
		int map[max_value+1];
		memset(map,0,sizeof(map));
		for(i=0;i<2*n-1;i++)
		{
			for(j=0;j<n;j++)
			{
				map[grid[i][j]]++;
			}
		}
		//for(i=0;i<=max_value;i++)
		//	printf("%d ",map[i]);
		//printf("\n");
		printf("Case #%d: ",t1);
		for(i=0;i<=max_value;i++)
		{
			if(map[i]%2!=0)
			{
				printf("%d ", i);
			}
		}
		printf("\n");
		t1++;
	}
	return 0;
}