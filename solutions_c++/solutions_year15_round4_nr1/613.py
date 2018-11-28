#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <cstring>
using namespace std;

typedef long long ll;
#define NN 128
char f[NN][NN];
int R, C;

int dirByChar(char c) {
	switch (c) {
		case '<': return 0;
		case '>': return 1;
		case '^': return 2;
		case 'v': return 3;
	}
	return 4;
}

int dy[5] = {0, 0, -1, 1, 0};
int dx[5] = {-1, 1, 0, 0, 0};

bool goodDir(int y, int x, int dir) {
	if (dir > 3) return true;
	y += dy[dir];
	x += dx[dir];
	while (y >= 0 && y < R && x >= 0 && x < C) {
		if (f[y][x] != '.') return true;
		y += dy[dir];
		x += dx[dir];
	}
	return false;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; ++i) {
			scanf("%s", f[i]);
		}
		int count = 0;
		for (int y = 0; y < R; ++y) {
			for (int x = 0; x < C; ++x) {
				int dir = dirByChar(f[y][x]);
				if (goodDir(y, x, dir)) continue;
				for (int dir = 0; dir < 4; ++dir) {
					if (goodDir(y, x, dir)) {
						++count;
						goto next;
					}
				}
				goto bad;
next:
				continue;
			}
		}
		printf("Case #%d: %d\n", ti+1, count);
		continue;
bad:
		printf("Case #%d: IMPOSSIBLE\n", ti+1);
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
