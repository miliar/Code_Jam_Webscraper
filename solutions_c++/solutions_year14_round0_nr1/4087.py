#include <bits/stdc++.h>
using namespace std;

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("ans.out", "w", stdout);
	int t,i,j,n,ra,rb, match = 0, ans;
	scanf("%d", &t);
	for(int cs = 1; cs<=t; cs++)
	{
		scanf("%d", &ra);
		match = 0;
		int a[4][4], pa[17] = {0}, b[4][4], pb[17]={0};
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				scanf("%d", &a[i][j]);
				pa[a[i][j]] = i+1;
			}
		}
		scanf("%d", &rb);
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				scanf("%d", &b[i][j]);
				pb[b[i][j]] = i+1;
			}
		}
		for(i=0; i<4; i++)
		{
			if(pb[a[ra-1][i]] == rb)
			{
				match++;
				ans = a[ra-1][i];
			}
		}
		printf("Case #%d: ", cs);
		if(match == 0)
			printf("Volunteer cheated!\n");
		else if(match == 1)
			printf("%d\n", ans);
		else
			printf("Bad magician!\n");
	}
	return 0;
}