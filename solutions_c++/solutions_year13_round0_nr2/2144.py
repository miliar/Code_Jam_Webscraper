#include <cstdio>
const int S = 100;
int lawn[S][S];
int sx, sy;
bool sqpossible(int x, int y)
{
	int d = 0;
	for (int i = 0; i < sx; i++)
	{
		if (lawn[i][y] > lawn[x][y])
		{
			d++;
			break;
		}
	}
	for (int j = 0; j < sy; j++)
	{
		if (lawn[x][j] > lawn[x][y])
		{
			d++;
			break;
		}
	}
	return d < 2;
}
int main()
{
	int t;
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		bool possible = true;
		scanf("%d%d", &sx, &sy);
		for (int j = 0; j < sx; j++)
			for (int k = 0; k < sy; k++)
				scanf("%d", &lawn[j][k]);
		for (int j = 0; j < sx; j++)
			for (int k = 0; k < sy; k++)
				possible = possible && sqpossible(j, k);
		printf("Case #%d: ", i);
		if (possible)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}