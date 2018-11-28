#include <stdio.h>
#include <stdlib.h>

int grass[100][100],m,n;

bool testmower(int x,int y)
{
	int curheight;
	int i;
	curheight = grass[x][y];
	int count = 0;
	for (i = 0; i<m; i++)
	{
		if (grass[i][y]<=curheight)
			count++;
	}
	if (count == m)
		return true;
	count = 0;
	for (i = 0; i<n; i++)
	{
		if (grass[x][i]<=curheight)
			count++;
	}
	if (count == n)
		return true;
	return false;
}

int main()
{
	int i,j,k;
	int cases;
	bool judge;
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d\n",&cases);
	for (i = 1; i<=cases; i++)
	{
		judge = true;
		scanf("%d %d\n",&m,&n);
		for (j = 0; j<m; j++)
		{
			for (k=0; k<n-1; k++)
			{
				scanf("%d ",&grass[j][k]);
			}
			scanf("%d\n",&grass[j][n-1]);
		}
		for (j = 0; j<m; j++)
		{
			for (k = 0; k<n; k++)
			{
				if (!testmower(j,k))
				{
					judge = false;
					break;
				}
			}
		}
		if (judge)
			printf("Case #%d: YES\n",i);
		else
			printf("Case #%d: NO\n",i);
	}
}
