//Yerzhan Dyussenaliyev
#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

#define N 10

int a[N][N], b[N][N], T, r1, r2, col, res;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &r1);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				scanf("%d", &a[i][j]);
		scanf("%d", &r2);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				scanf("%d", &b[i][j]);
		col = 0;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				if (a[r1][i] == b[r2][j])
				{
					col++;
					res = a[r1][i];
				}
		printf("Case #%d: ", t);
		if (col == 1)
			printf("%d\n", res);
		else
		if (col > 1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}

    return 0;
}
