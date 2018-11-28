#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int G[10][10];
bool vst[10][10];
int R, C, M;
int dx[8] = {-1, 0, 1, 0, -1, 1, -1, 1};
int dy[8] = {0, 1, 0, -1, 1, -1, -1, 1};
char ones[(1 << 25) + 5];

bool in(int x, int y)
{
	return (x >= 0 && y >= 0 && x < R && y < C);
}

int calOnes(int s)
{
	int ret = 0;
	while (s)
	{
		ret += s & 1;
		s >>= 1;
	}
	return ret;
}

void dfs(int r, int c)
{
	vst[r][c] = true;
	if (G[r][c] > 0) return ;
	for (int d = 0; d < 8; d++)
	{
		int nr = r + dx[d], nc = c + dy[d];
		if (!in(nr, nc)) continue;
		if (G[nr][nc] == -1) continue;
		if (vst[nr][nc]) continue;
		dfs(nr, nc);
	}
}

bool canOneClick(int r, int c)
{
	memset(vst, 0, sizeof(vst));
	dfs(r, c);
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++)
			if (!vst[i][j] && G[i][j] != -1)
				return false;
	return true;
}

bool check(int s)
{
	memset(G, 0, sizeof(G));
	for (int r = 0; r < R; r++)
		for (int c = 0; c < C; c++)
			if (s & (1 << (r * C + c)))
				G[r][c] = -1;
	for (int r = 0; r < R; r++)
	{
		for (int c = 0; c < C; c++)
		{
			if (G[r][c] == -1) continue;
			for (int d = 0; d < 8; d++)
			{
				int nr = r + dx[d], nc = c + dy[d];
				if (!in(nr, nc)) continue;
				if (G[nr][nc] == -1) G[r][c]++;
			}
		}
	}
	bool clicked = false;
	for (int r = 0; r < R; r++)
	{
		for (int c = 0;c < C; c++)
		{
			if (G[r][c] == -1) continue;
			if (canOneClick(r, c))
			{
				G[r][c] = -2;
				return true;
			}
		}
	}
	return false;
}

int main()
{
	freopen("C-small-attempt3.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	for (int s = 0; s < (1 << 25); s++)
		ones[s] = calOnes(s);
	int _, cases = 1;
	cin >> _;
	while (_--)
	{
		cin >> R >> C >> M;
		printf("Case #%d:\n", cases++);
		bool done = false;
		for (int s = 0; s < (1 << (R * C)); s++)
		{
			if (ones[s] != M) continue;
			if (check(s))
			{
				done = true;
				bool clicked = false;
				for (int i = 0; i < R; i++)
				{
					for (int j = 0; j < C; j++)
					{
						if (G[i][j] == -1) printf("*");
						else if (G[i][j] >= 0) printf(".");
						else printf("c");
					}
					printf("\n");
				}
				break;
			}
		}
		if (!done) puts("Impossible");
	}
	return 0;
}