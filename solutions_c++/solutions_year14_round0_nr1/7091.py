#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

bool use[20];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int q = 0; q < t; q++)
	{
		memset(use, false, sizeof(use));
		int cnt = 0, last = -1;
		for (int c = 0; c < 2; c++)
		{
			int k;
			scanf("%d", &k);
			for (int i = 0; i < 4; i++)
			{
				for (int j = 0; j < 4; j++)
				{
					int x;
					scanf("%d", &x);
					if (c == 0 && k - 1 == i)
					{
						use[x] = true;
					}
					if (c == 1 && k - 1 == i && use[x])
					{
						cnt++;
						last = x;
					}
				}
			}
		}
		printf("Case #%d: ", q + 1);
		if (cnt == 1)
		{
			printf("%d\n", last);
		}
		else
		{
			if (cnt == 0)
			{
				printf("Volunteer cheated!\n");
			}
			else
			{
				printf("Bad magician!\n");
			}
		}
	}
	return 0;
}