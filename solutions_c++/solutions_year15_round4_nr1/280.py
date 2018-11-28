#include <iostream>
#include <cstdio>
using namespace std;

const int ND = 4;
const int DX[] = {-1, 0, 0, 1};
const int DY[] = {0, -1, 1, 0};

const int MaxR = 100;
const int MaxC = 100;

int r, c;
char a[MaxR + 2][MaxC + 2];

int solve()
{
	static bool book[MaxR + 2][MaxC + 2];
	for (int x = 1; x <= r; x++)
		for (int y = 1; y <= c; y++)
			book[x][y] = false;
	for (int x = 1; x <= r; x++)
		for (int y = 1; y <= c; y++)
			if (a[x][y] != '.')
			{
				book[x][y] |= a[x][y] == '<';
				break;
			}
	for (int x = 1; x <= r; x++)
		for (int y = c; y >= 1; y--)
			if (a[x][y] != '.')
			{
				book[x][y] |= a[x][y] == '>';
				break;
			}
	for (int y = 1; y <= c; y++)
		for (int x = 1; x <= r; x++)
			if (a[x][y] != '.')
			{
				book[x][y] |= a[x][y] == '^';
				break;
			}
	for (int y = 1; y <= c; y++)
		for (int x = r; x >= 1; x--)
			if (a[x][y] != '.')
			{
				book[x][y] |= a[x][y] == 'v';
				break;
			}

	int res = 0;
	for (int vx = 1; vx <= r; vx++)
		for (int vy = 1; vy <= c; vy++)
			if (book[vx][vy])
				res++;
	for (int vx = 1; vx <= r; vx++)
		for (int vy = 1; vy <= c; vy++)
			if (book[vx][vy])
			{
				for (int d = 0; d <= ND; d++)
				{
					if (d == ND)
						return -1;
					int x = vx + DX[d], y = vy + DY[d];
					while (1 <= x && x <= r && 1 <= y && y <= c && a[x][y] == '.')
						x += DX[d], y += DY[d];
					if (1 <= x && x <= r && 1 <= y && y <= c)
						break;
				}
			}
	return res;
}

int main()
{
	int nT;
	cin >> nT;
	for (int nt = 1; nt <= nT; nt++)
	{
		scanf("%d %d", &r, &c);
		for (int x = 1; x <= r; x++)
			scanf("%s", a[x] + 1);

		printf("Case #%d: ", nt);
		int res = solve();
		if (res != -1)
			printf("%d", res);
		else
			printf("IMPOSSIBLE");
		printf("\n");
	}

	return 0;
}
