#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

void solve()
{
	int row1, row2, i, j, k, l, ans, sum = 0;
	int CHESS[4];

	scanf("%d", &row1);
	for (i = 0; i < 4; i++)
	{
		if (i != row1 - 1){
			for (j = 0; j < 4; j++)
			{
				scanf("%d", &k);
			}
		}
		if (i == row1 - 1){
			for (j = 0; j < 4; j++)
			{
				scanf("%d", &CHESS[j]);
			}
		}
	}
	scanf("%d", &row2); 
	for (i = 0; i < 4; i++)
	{
		if (i != row2 - 1){
			for (j = 0; j < 4; j++)
			{
				scanf("%d", &k);
			}
		}
		if (i == row2 - 1){
			for (j = 0; j < 4; j++)
			{
				scanf("%d", &k);
				for (l = 0; l < 4; l++)
				{
					if (k == CHESS[l])
					{
						sum += 1;
						ans = k;
					}
				}
			}
		}
	}
	if (sum > 1)
	{
		printf("Bad magician!\n");
	}
	else if (sum == 1)
	{
		printf("%d\n", ans);
	}
	else
	{
		printf("Volunteer cheated!\n");
	}

	
}

int main()
{
	int T;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}