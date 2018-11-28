#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <queue>
#include <cstring>
using namespace std;


int T, R, C;
char a[105][105];
int l[105], r[105], t[105], b[105];

int f() {
	int ret = 0;
	for (int i = 0; i < R; ++i) {
		for (int j = 0; j < C; ++j) {
			if (a[i][j] == '^') {
				if (t[j] == i) {
					if (l[i] == j && r[i] == j && b[j] == i) return -1;
					ret++;
				}
			}
			else if (a[i][j] == 'v') {
				if (b[j] == i) {
					if (l[i] == j && r[i] == j && t[j] == i) return -1;
					ret++;
				}
			}
			else if (a[i][j] == '<') {
				if (l[i] == j) {
					if (r[i] == j && t[j] == i && b[j] == i) return -1;
					ret++;
				}
			}
			else if (a[i][j] == '>') {
				if (r[i] == j) {
					if (l[i] == j && t[j] == i && b[j] == i) return -1;
					ret++;
				}
			}
		}
	}
	return ret;
}

int main(){
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; ++i) {
			scanf("%s", a[i]);
		}
		for (int i = 0; i <= 100; ++i) {
			l[i] = 1000;
			r[i] = -1;
			t[i] = 1000;
			b[i] = -1;
		}
		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				if (a[i][j] != '.') {
					l[i] = min(l[i], j);
					r[i] = max(r[i], j);
					t[j] = min(t[j], i);
					b[j] = max(b[j], i);
				}
			}
		}
		int ans = f();
		if (ans == -1) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
		}
		else {
			printf("Case #%d: %d\n", tc, ans);
		}
	}

	return 0;
}