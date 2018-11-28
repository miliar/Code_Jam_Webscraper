#include <cassert>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <utility>

using namespace std;

struct Pair { int a, b; };

int R, C;
Pair pairs[200];
char maze[105][105];

int visited[1000];

int N1, N2, N;

int getNode(int x) {
	assert(x >= 1);
	x--;
	if (x < C) {
		return x;
	}
	x -= C;
	if (x < R) {
		return N1 + C*R + x;
	}
	x -= R;
	if (x < C) {
		return R*C + C-1-x;
	}
	x -= C;
	assert(x < R);
	return N1 + R-1-x;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d:\n", t);
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R+C; i++) {
			int a, b;
			scanf("%d%d", &a, &b);
			pairs[i] = (Pair) { a, b };
			//printf("# pair %d %d\n", a, b);
		}
		N1 = (R+1)*C;
		N2 = (C+1)*R;
		N = N1+N2;
		/*printf("# R=%d C=%d\n", R, C);
		printf("N1=%d N2=%d\n", N1, N2);*/
		bool possible = false;
		for (int mask = 0; mask < (1 << (R*C)); mask++) {
			for (int r = 0; r < R; r++) {
				for (int c = 0; c < C; c++) {
					maze[r][c] = (mask & (1 << (r*C+c))) ? '\\' : '/';
				}
			}
			/*printf("# attempt\n");
			for (int r = 0; r < R; r++) {
				printf("# ");
				for (int c = 0; c < C; c++) {
					printf("%c", maze[r][c]);
				}
				printf("\n");
			}*/
			vector<vector<int> > adj(N);
			for (int r = 0; r < R; r++) {
				for (int c = 0; c < C; c++) {
					int x1 = r * C + c, x4 = (r + 1) * C + c;
					int x2 = N1 + c * R + r, x3 = N1 + (c + 1) * R + r;
					if (maze[r][c] == '/') {
						adj[x1].push_back(x2);
						adj[x2].push_back(x1);
						adj[x3].push_back(x4);
						adj[x4].push_back(x3);
					} else {
						adj[x1].push_back(x3);
						adj[x3].push_back(x1);
						adj[x2].push_back(x4);
						adj[x4].push_back(x2);
					}
				}
			}
			bool ok = true;
			for (int i = 0; i < R+C; i++) {
				Pair p = pairs[i];
				int a = getNode(p.a), b = getNode(p.b);
				//printf("# pair %d %d - nodes %d %d\n", p.a, p.b, a, b);
				int prev = -1, current = a;
				while (true) {
					int next = -1;
					assert(adj[current].size() >= 1);
					assert(adj[current].size() <= 2);
					for (int j = 0; j < (int) adj[current].size(); j++) {
						int node = adj[current][j];
						if (node != prev) {
							next = node;
							break;
						}
					}
					if (next == -1) {
						break;
					}
					prev = current;
					current = next;
				}
				//printf("# pair %d %d - nodes %d %d, connected=%d\n", p.a, p.b, a, b, current == b);
				if (current != b) {
					ok = false;
					break;
				}
			}
			if (ok) {
				possible = true;
				break;
			}
		}
		if (possible) {
			for (int r = 0; r < R; r++) {
				for (int c = 0; c < C; c++) {
					printf("%c", maze[r][c]);
				}
				printf("\n");
			}
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
