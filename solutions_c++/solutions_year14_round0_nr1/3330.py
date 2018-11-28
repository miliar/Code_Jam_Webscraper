#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int a[5][5], b[5][5], ans[4];
int t, n, m, f;

int main()
{
	scanf("%d",&t);
	int c, i, j;
	for (c = 1; c <= t; c++)
	{
		scanf("%d",&n);
		for (i = 1; i <= 4; i++)
			for (j = 1; j <= 4; j++)
				scanf("%d",&a[i][j]);
		scanf("%d",&m);
		for (i = 1; i <= 4; i++)
			for (j = 1; j <= 4; j++)
				scanf("%d",&b[i][j]);
		f = 0;
		for (i = 1; i <= 4; i++)
		for (j = 1; j <= 4; j++)
		if (a[n][i] == b[m][j])
			ans[f++] = a[n][i];
		printf("Case #%d: ",c);
		switch(f)
		{
			case 0:
				printf("Volunteer cheated!\n");
				break;
			case 1:
				printf("%d\n",ans[0]);
				break;
			default:
				printf("Bad magician!\n");
				break;
		}
		
	}
	return 0;
}

