#include <cstdio>
#include <cstring>

using namespace std;

//const char CASE[] = "^v<>";

const int RC = 100 + 10, NCASE = 4;
char map[RC][RC];

bool b[RC][RC][NCASE];

int main()
{
	int T;
	scanf("%d", &T);

	for(int ca = 1; ca <= T; ++ca) {
		int r, c;
		scanf("%d%d", &r, &c);
		for(int i = 0; i < r; ++i)
			scanf("%s", map[i]);

		memset(b, 0, sizeof(b));

		for(int i = 0; i < c; ++i)
			for(int j = 0; j < r; ++j)
				if(map[j][i] != '.') {
					b[j][i][0] = true;
					break;
				}

		for(int i = 0; i < c; ++i)
			for(int j = r - 1; j >= 0; --j)
				if(map[j][i] != '.') {
					b[j][i][1] = true;
					break;
				}

		for(int i = 0; i < r; ++i)
			for(int j = 0; j < c; ++j)
				if(map[i][j] != '.') {
					b[i][j][2] = true;
					break;
				}

		for(int i = 0; i < r; ++i)
			for(int j = c - 1; j >= 0; --j)
				if(map[i][j] != '.') {
					b[i][j][3] = true;
					break;
				}

		int ans = 0;

		for(int i = 0; i < r; ++i) {
			for(int j = 0; j < c; ++j)
				if(map[i][j] != '.') {
					if(b[i][j][0] && b[i][j][1] && b[i][j][2] && b[i][j][3]) {
						ans = -1;
						break;
					}
					if(
					(map[i][j] == '^' && b[i][j][0]) ||
					(map[i][j] == 'v' && b[i][j][1]) ||
					(map[i][j] == '<' && b[i][j][2]) ||
					(map[i][j] == '>' && b[i][j][3])
					)
						++ans;
				}

			if(ans < 0) break;
		}

		if(ans < 0)
			printf("Case #%d: IMPOSSIBLE\n", ca);
		else
			printf("Case #%d: %d\n", ca, ans);
	}
}