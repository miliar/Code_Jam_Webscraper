#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int n, m;
int map[200][200];

int solve() {
	for (int h = 100; h > 0; --h) {
		for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j)
			if (map[i][j] == h) {
				int state = 3;
				for (int k = 0; k < n; ++k) 
					if (k != i && map[k][j] > h) { state -= 1; break; }
				for (int k = 0; k < m; ++k) 
					if (k != j && map[i][k] > h) { state -= 2; break; }
				if (state == 0) return 0;
			}
	}
	return 1;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int c = 1; c <= t; ++c) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j) scanf("%d", map[i] + j);
		printf("Case #%d: %s\n", c, solve() ? "YES" : "NO");
	}
}