#include <cstdio>
#include <intrin.h>

using namespace std;

int R, C, M;
bool next_combination(int& comb, int n) {
	int x = comb & -comb, y = comb + x;
	comb = ((comb & ~y) / x >> 1) | y;
	return (comb < 1 << n);
}

int dy[] = { 0, 0, 1, -1, 1, 1, -1, -1 };
int dx[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int visited;

bool isin(int x, int y) {
	return (0 <= x && x < C && 0 <= y && y < R);
}

int dfs(int pos, int bit) {
	if ((visited >> pos) & 1) {
		return 0;
	}
	visited |= 1 << pos;
	int x = pos % C;
	int y = pos / C;
	bool ok = true;
	for (int i = 0; i < 8; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (!isin(nx, ny)) {
			continue;
		}
		int npos = nx + ny* C;
		if ((bit >> npos) & 1) {
			ok = false;
			continue;
		}
	}
	if (!ok) {
		return 1;
	}
	int res = 1;
	for (int i = 0; i < 8; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (!isin(nx, ny)) {
			continue;
		}
		int npos = nx + ny* C;
		res += dfs(npos, bit);
	}
	return res;
}

int findzero(unsigned int bit) {
	for (int i = 0; i < 32; i++) {
		if (((bit >> i) & 1) == 0) {
			return i;
		}
	}
}

void small() {
	int N = R * C;
	if (M == N) {
		printf("Impossible\n");
		return;
	}
	int comb = (1 << M) - 1;
	do {
		int pos = findzero(comb);
		visited = 0;
		int cnt = dfs(pos, comb);
		if (cnt > (N - M)) throw 0;
		if (cnt == (N - M)) {
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					int p = i * C + j;
					if (p == pos) {
						printf("c");
					}
					else {
						printf("%c", ((comb >> p) & 1) ? '*' : '.');
					}
				}
				printf("\n");
			}
			return;
		}
	} while (next_combination(comb, N));
	printf("Impossible\n");
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d %d %d", &R, &C, &M);
		printf("Case #%d:\n", tc + 1);
		small();
	}
}