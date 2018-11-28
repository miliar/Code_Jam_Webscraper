#include<cstdio>
#include<algorithm>

using namespace std;

int T, N, M, a[105][105], max1[105], max2[105], boo;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int g = 0; g < T; g++)
	{
		boo = 0;
		scanf("%d%d", &N, &M);
		for (int i = 0; i < N; i++)
			max1[i] = -1;
		for (int i = 0; i < M; i++)
			max2[i] = -1;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
			{
				scanf("%d", &a[i][j]);
				max1[i] = max(max1[i], a[i][j]);
				max2[j] = max(max2[j], a[i][j]);
			}
		for (int i = 0; i < N; i++)
		{
		    if (boo == 1)
		    	break;
			for (int j = 0; j < M; j++)
				if (a[i][j] != max1[i] && a[i][j] != max2[j])
				{
					printf("Case #%d: NO\n", g + 1);
					boo = 1;
					break;
				}
		}
		if (boo == 1)
			continue;
		printf("Case #%d: YES\n", g + 1);
	}
}
