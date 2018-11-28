#include <cstdio>

const int SZ = 128;
const int DIR[4][2]={{0,1},{1,0},{0,-1},{-1,0}};
int graph[SZ][SZ];
int N, M;

bool check(int row, int col) {
	int me = graph[row][col];
	bool first = true;
	for (int j = 0; j < M; ++j) {
		if (graph[row][j] > me) {
			first = false;
		}
	}
	if (first) {
		for (int j = 0; j < M; ++j) {
			graph[row][j] = 0;
		}
	}
	bool second = true;
	for (int i = 0; i < N; ++i) {
		if (graph[i][col] > me) {
			second = false;
		}
	}
	if (second) {
		for (int i = 0; i < N; ++i) {
			graph[i][col] = 0;
		}
	}
	return graph[row][col] == 0;
}

int main() {
	int K;
	scanf("%d", &K);
	for (int kase = 0; kase < K; ++kase) {
		scanf("%d%d", &N, &M);
		int maxh = 0;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < M; ++j) {
				scanf("%d", &graph[i][j]);
				if (graph[i][j] > maxh) maxh = graph[i][j];
			}
		}
		bool ret = true;
		for (int h = 0; h < maxh; ++h) {
			for (int i = 0; i < N; ++i) {
				for (int j = 0; j < M; ++j) {
					if (graph[i][j] == h) {
						if (!check(i, j)) {
							ret = false;
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: %s\n", kase + 1, ret ? "YES" : "NO");
	}
	return 0;
}
