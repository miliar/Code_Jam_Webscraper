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

const int dx[4] = {0, 0, -1, 1};
const int dy[4] = {-1, 1, 0, 0};

struct rec
{
	int a, b;
};

int n;
char a[5][5], ans;
bool ok;

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	#endif

	scanf("%d\n", &n);
	for (int T = 1; T <= n; T++)
	{
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1; j <= 4; j++)
				scanf("%c", &a[i][j]);
			scanf("\n");
		}
		scanf("\n");
		printf("Case #%d: ", T);
		ok = false;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				if (a[i][j] == 'X' || a[i][j] == 'O')
				if ((j + 3 <= 4 && a[i][j] == a[i][j + 1] && a[i][j] == a[i][j + 2] && (a[i][j] == a[i][j + 3] || a[i][j + 3] == 'T')) || 
					(i + 3 <= 4 && a[i][j] == a[i + 1][j] && a[i][j] == a[i + 2][j] && (a[i][j] == a[i + 3][j] || a[i + 3][j] == 'T')) || 
					(i + 3 <= 4 && j + 3 <= 4 && a[i][j] == a[i + 1][j + 1] && a[i][j] == a[i + 2][j + 2] && (a[i][j] == a[i + 3][j + 3] || a[i + 3][j + 3] == 'T')) || 
					(i + 3 <= 4 && j - 3 >= 1 && a[i][j] == a[i + 1][j - 1] && a[i][j] == a[i + 2][j - 2] && (a[i][j] == a[i + 3][j - 3] || a[i + 3][j - 3] == 'T')))
					{
						ok = true;
						ans = a[i][j];
					}
		if (ok)
			printf("%c won\n", ans);
		else
		{
			for (int i = 1; i <= 4; i++)
				for (int j = 1; j <= 4; j++)
					if (a[i][j] == '.')
			           	ok = true;
			if (ok)
				printf("Game has not completed\n");
			else
				printf("Draw\n");
		}
	}

    return 0;
}
