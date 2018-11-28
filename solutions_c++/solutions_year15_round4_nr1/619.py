#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
using namespace std;

char mp[105][105];
int n, m;

int in(int x, int y) {
	return x >= 0 && x < n && y >= 0 && y < m;
}
const int step[8][2] = {
	{-1, 0}, {0, 1}, {1, 0}, {0, -1}, {-1, 1}, {1, 1}, {1, -1}, {-1, -1}};

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("alargeout.txt", "w", stdout);
	int t, ca = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			scanf("%s", mp[i]);
		printf("Case #%d: ", ca++);
		int ans = 0;
		int rflag = 1;
		for (int i = 0; i < n && rflag; i++)
			for (int j = 0; j < m && rflag; j++)
				if (mp[i][j] != '.') {
					int dx = 0, dy = 0;
					if (mp[i][j] == '^')
						dx = -1, dy = 0;
					if (mp[i][j] == '<')
						dx = 0, dy = -1;
					if (mp[i][j] == '>')
						dx = 0, dy = 1;
					if (mp[i][j] == 'v')
						dx = 1, dy = 0;
					int ri = i + dx, rj = j + dy;
					while (in(ri, rj) && mp[ri][rj] == '.')
						ri += dx, rj += dy;
					if (!in(ri, rj)) {
						bool flag = 0;
						for (int k = 0; k < 4; k++) {
							dx = step[k][0], dy = step[k][1];
							ri = i + dx, rj = j + dy;
							while (in(ri, rj) && mp[ri][rj] == '.') {
								ri += dx, rj += dy;
							}
							if (in(ri, rj))
								flag = 1;
						}
						if (flag)
							ans++;
						else
							rflag = 0;
					}
				}
		if (rflag)
			printf("%d\n", ans);
		else
			puts("IMPOSSIBLE");
	}
	return 0;
}
