#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, T;
	int i, j, k;
	char used[4];
	int cnt;
	int card;
	int r;
	int tmp;
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d", &r);
		for (i = 0; i < 4; i++)
		{
			for (j = 0; j < 4; j++)
			{
				scanf("%d", &tmp);
				if (i == r - 1)
				{
					used[j] = tmp;
				}
			}
		}
		scanf("%d", &r);
		cnt = 0;
		for (i = 0; i < 4; i++)
		{
			for (j = 0; j < 4; j++)
			{
				scanf("%d", &tmp);
				if (i == r - 1)
				{
					for (k = 0; k < 4; k++)
					{
						if (used[k] == tmp) 
						{
							cnt++;
							card = tmp;
						}
					}
				}
			}
		}
		printf("Case #%d: ", t);
		if (cnt == 0) printf("Volunteer cheated!\n");
		else if (cnt == 1) printf("%d\n", card);
		else printf("Bad magician!\n");
	}
	return 0;
}