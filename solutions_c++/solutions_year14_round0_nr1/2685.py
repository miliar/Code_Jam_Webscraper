#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
	int t, i, j, ca, f, e,c,x;
	int a[4][4], b[4][4];
	scanf("%d", &t);
	for (ca = 1; ca <= t; ca++)
	{
		scanf("%d", &f);
		for (i = 0; i < 4; i++)
		{
			for (j = 0; j < 4; j++)
			{
				scanf("%d", &a[i][j]);
			}
		}
		scanf("%d", &e);
		for (i = 0; i < 4; i++)
		{
			for (j = 0; j < 4; j++)
			{
				scanf("%d", &b[i][j]);
			}
		}
		c = 0;
		x = -1;
		for (i = 0; i < 4; i++)
		{
			for (j = 0; j < 4; j++)
			{
				if (a[f - 1][i] == b[e - 1][j])
				{
					c++;
					x = a[f - 1][i];
				}
			}
		}
		printf("Case #%d: ",ca);
		if (c == 1)
		{
			printf("%d\n", x);
		}
		else if (c==0)
		{
			puts("Volunteer cheated!");
		}
		else
		{
			puts("Bad magician!");
		}
	}
}