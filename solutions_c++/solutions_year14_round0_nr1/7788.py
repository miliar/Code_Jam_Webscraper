#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int a[4][4], b[4][4];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int task;
	scanf("%d", &task);
	for (int _i = 1; _i <= task; ++_i)
	{
		int x, y;
		scanf("%d", &x);
		--x;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf("%d", &a[i][j]);
		scanf("%d", &y);
		--y;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf("%d", &b[i][j]);
			/*
		for (int i = 0; i < 4; ++i)
			printf("%d ", a[x][i]);
		puts("");
		for (int i = 0; i < 4; ++i)
			printf("%d ", b[y][i]);
		puts("");*/
		int s = 0, t = -1;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (a[x][i] == b[y][j])
				{
					++s, t = a[x][i];
					//printf("fff %d %d\n", i, j);
				}
		if (s == 0)
			printf("Case #%d: Volunteer cheated!\n", _i);
		else if (s == 1)
			printf("Case #%d: %d\n", _i, t);
		else 
			printf("Case #%d: Bad magician!\n", _i);
	}

	return 0;
}