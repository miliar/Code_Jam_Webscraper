#include <iostream>
#include <cstdio>
#include <stdio.h>
using namespace std;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int T;
	int fans,sans;
	int magic1[4][4];
	int magic2[4][4];
	scanf("%d",&T);
	for (int t = 0; t < T; ++t)
	{
		scanf("%d",&fans);
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				scanf("%d",&magic1[i][j]);
			}
		}
		scanf("%d",&sans);
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				scanf("%d",&magic2[i][j]);
			}
		}
		int findAns = -1;
		int res = -1;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				if (magic1[fans-1][i] == magic2[sans-1][j])
				{
					if (findAns == -1)
					{
						findAns = magic1[fans-1][i];
					}
					else if (findAns != magic1[fans-1][i])
					{
						res = 0;
					}
				}
			}
		}
		printf("Case #%d: ",t+1);
		if (res == 0)
		{
			printf("Bad magician!\n");
		}
		else if (findAns == -1)
		{
			printf("Volunteer cheated!\n");
		}
		else
		{
			printf("%d\n",findAns);
		}
	}
	return 0;
}