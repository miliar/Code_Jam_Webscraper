#include <cstdio>

//#define small
#define large

const int mX[] = {-1, 0, 1, 0};
const int mY[] = {0, 1, 0, -1};

int t, n, m;
char inp[105][105];

int change(const char& c) {
	if (c == '^')
		return 0;
	if (c == '>')
		return 1;
	if (c == 'v')
		return 2;
	return 3;
}

int main()
{
#ifdef small
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
#endif
#ifdef large
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	scanf("%d", &t);
	for (int Case = 1; Case <= t; ++Case) {
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; ++i)
			scanf("%s", inp[i]);
		int ans = 0;
		for (int i = 0; i < n && ans != -1; ++i) {
			for (int j = 0; j < m; ++j) {
				if (inp[i][j] == '.')
					continue;
				int temp = 0;
				for (int d = 0; d < 4; ++d) {
					int x = i + mX[d], y = j + mY[d];
					while (x >= 0 && x < n && y >= 0 && y < m && inp[x][y] == '.')
						x += mX[d], y += mY[d];
					if (x < 0 || x >= n || y < 0 || y >= m)
						temp += 1 << d;
				}
				if (temp == 15) {
					ans = -1;
					break;
				}
				if (temp & (1 << change(inp[i][j])))
					++ans;
			}
		}
		printf("Case #%d: ", Case);
		if (ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}
