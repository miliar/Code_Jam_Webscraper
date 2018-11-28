#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int k = 1; k <= t; k++)
	{
		int ans1, ans2;
		int a[4][4], b[4][4];
		scanf("%d", &ans1);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d", &a[i][j]);
		scanf("%d", &ans2);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d", &b[i][j]);
		ans1--; ans2--;
		int count = 0, ans = -1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (b[ans2][j] == a[ans1][i])
				{
					ans = b[ans2][j];
					count++;
				}
		if (count == 1)
			printf("Case #%d: %d\n", k, ans);
		else if (count == 0)
			printf("Case #%d: Volunteer cheated!\n", k);
		else
			printf("Case #%d: Bad magician!\n", k);
	}
	return 0;
}