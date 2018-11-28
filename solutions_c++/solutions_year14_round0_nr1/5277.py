#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int mask;
int grid[5][5];

void gao()
{
	int r;
	scanf("%d", &r);
	for (int i = 1; i <= 4; ++i) for (int j = 1; j <= 4; ++j) scanf("%d", &grid[i][j]);
	int curmask = 0;
	for (int j = 1; j <= 4; ++j) curmask |= 1 << (grid[r][j] - 1);
	mask &= curmask;
}

void work()
{
	mask = (1 << 16) - 1;
	gao();
	gao();
	static int ttt = 0;
	printf("Case #%d: ", ++ttt);
	if (mask == 0) {
		printf("Volunteer cheated!\n");
	} else if ((mask & -mask) != mask)
		printf("Bad magician!\n");
	else {
		for (int i = 1; i <= 16; ++i) if ((1 << (i - 1)) == mask) printf("%d\n", i);
	}
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	while (T--) work();
}