#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int T, s[10][10], a;
int sum[20];

int main()
{
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++)
	{
		memset(sum, 0, sizeof(sum));
		for (int x = 1; x <= 2; x++)
		{
			scanf("%d", &a);
			for (int i = 1; i <= 4; i++)
				for (int j = 1; j <= 4; j++)
				{
					scanf("%d", &s[i][j]);
				}
			for (int j = 1; j <= 4; j++)
			{
				sum[s[a][j]]++;
			}
		}
		int k = 0;
		for (int i = 1; i <= 16; i++)
			if (sum[i] == 2) k++;
		printf("Case #%d: ", tt);
		if (k == 0)
			puts("Volunteer cheated!");
		else if (k >= 2)
			puts("Bad magician!");
		else for (int i = 1; i <= 16; i++)
			if (sum[i] == 2) printf("%d\n", i);
	}
	return 0;
}
