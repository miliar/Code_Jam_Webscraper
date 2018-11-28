#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int t, row, col, l[110], r[110], u[110], d[110];
char s[110][110];

int main()
{
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		scanf("%d%d", &row, &col);
		for (int i = 0; i < row; ++i)
			scanf("%s", s[i]);

		memset(l, -1, sizeof(l));
		memset(r, -1, sizeof(r));
		memset(u, -1, sizeof(u));
		memset(d, -1, sizeof(d));
		for (int i = 0; i < row; ++i)
			for (int j = 0; j < col; ++j)
				if (s[i][j] != '.') {
					if (l[i] == -1) l[i] = j;
					r[i] = j;
				}
		for (int j = 0; j < col; ++j)
			for (int i = 0; i < row; ++i)
				if (s[i][j] != '.') {
					if (u[j] == -1) u[j] = i;
					d[j] = i;
				}

		bool flag = true;
		for (int i = 0; i < row; ++i)
			for (int j = 0; j < col; ++j)
				if (s[i][j] != '.') {
					if (l[i] == j && r[i] == j && u[j] == i && d[j] == i)
						flag = false;
						break;
				}
		if (!flag)
			printf("Case #%d: IMPOSSIBLE\n", tt);
		else {
			int ret = 0;
			for (int i = 0; i < row; ++i)
				if (l[i] != -1 && s[i][l[i]] == '<') ++ret;
			for (int i = 0; i < row; ++i)
				if (r[i] != -1 && s[i][r[i]] == '>') ++ret;
			for (int j = 0; j < col; ++j)
				if (u[j] != -1 && s[u[j]][j] == '^') ++ret;
			for (int j = 0; j < col; ++j)
				if (d[j] != -1 && s[d[j]][j] == 'v') ++ret;
			printf("Case #%d: %d\n", tt, ret);
		}
	}
	return 0;
}
