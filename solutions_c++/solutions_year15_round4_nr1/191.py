#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

char map[200][200];

int dir[200][2];
int nxt[200];
int n, m;

bool valid(int x, int y)
{
	if(x < 1 || x > n || y < 1 || y > m)
		return false;
	return true;
}

bool try_sim(int x, int y, int dx, int dy)
{
	x += dx, y += dy;
	while(valid(x, y))
	{
		if(map[x][y] != '.')
			return false;
		x += dx, y += dy;
	}
	return true;
}

int main()
{
	dir['^'][0] = -1, dir['^'][1] = 0;
	dir['v'][0] = 1, dir['v'][1] = 0;
	dir['>'][0] = 0, dir['>'][1] = 1;
	dir['<'][0] = 0, dir['<'][1] = -1;
	nxt['^'] = 'v';
	nxt['v'] = '>';
	nxt['>'] = '<';
	nxt['<'] = '^';
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas)
	{
		scanf("%d%d", &n, &m);
		for(int i = 1; i <= n; ++i)
			scanf("%s", map[i] + 1);
		printf("Case #%d: ", cas);
		int ans = 0;
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= m; ++j)
			{
				if(map[i][j] != '.')
				{
					int delta = 1;
					bool succ = false;
					char c = map[i][j];
					for(int t = 0; t < 4; ++t)
					{
						if(!try_sim(i, j, dir[c][0], dir[c][1]))
						{
							succ = true;
							delta = min(delta, (t == 0 ? 0 : 1));
						}
						c = nxt[c];
					}
					if(!succ)
						delta = 100000;
					ans += delta;
				}
			}
			if(ans >= 100000)
				printf("IMPOSSIBLE\n");
			else
				printf("%d\n", ans);
	}
	return 0;
}
