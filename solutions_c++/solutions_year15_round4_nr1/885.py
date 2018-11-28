//============================================================================
// Name        : gcj_a.cpp
// Author      : huangxs139
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int n, m;
char s[110][110];
bool orig[110][110];
int dir[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
int ans;

bool check(int x, int y) {
	if (x >= 0 && x < n && y >= 0 && y < m)
		return 1;
	return 0;
}

void solve(int ux, int uy, int ud) {
	int vx, vy, vd;
	bool c;
	int i;
	i = 1;
	while (1) {
		vx = ux + dir[ud][0]*i;
		vy = uy + dir[ud][1]*i;
		c = check(vx, vy);
		if (!c)	break;
		if (c && s[vx][vy] != '.') {
			orig[vx][vy] = 1;
			break;
		}
		i++;
	}
	if (!c) {
		ans++;
		for (vd = 0; vd < 4; vd++) {
			if (vd == ud)	continue;
			i = 1;
			while (1) {
				vx = ux + dir[vd][0]*i;
				vy = uy + dir[vd][1]*i;
				c = check(vx, vy);
				if (!c)	break;
				if (c && s[vx][vy] != '.') {
					orig[vx][vy] = 1;
					break;
				}
				i++;
			}
			if (c)	break;
		}
		if (vd == 4) {
			ans = -1;
			return;
		}
	}
	return;
}

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d: ", cas);
		ans = 0;
		memset(orig, 0, sizeof(orig));
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++)
			scanf("%s", s[i]);
		for (int i = 0; i < n && ans != -1; i++)
			for (int j = 0; j < m && ans != -1; j++) {
				switch(s[i][j]) {
				case '^':
					solve(i, j, 0);
					break;
				case '>':
					solve(i, j, 1);
					break;
				case 'v':
					solve(i, j, 2);
					break;
				case '<':
					solve(i, j, 3);
					break;
				default:
					break;
				}
			}
		if (ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}
