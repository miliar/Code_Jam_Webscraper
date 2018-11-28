//#include <cstdio>
//
//char maze[31][32];
//int dx[] = { 0, 1, 0, -1 }, dy[] = { 1, 0, -1, 0 };
//
//int DFS(int x, int y) {
//	if (maze[x][y] == '#') return 0;
//	if (maze[x][y] == 'G') return 1;
//	int ans = 0;
//	maze[x][y] = '#';
//	for (int i = 0; i < 4; i++) {
//		ans += DFS(x + dx[i], y + dy[i]);
//	}
//	maze[x][y] = '.';
//	return ans;
//}
//
//int main() {
//	freopen("maze.txt", "r", stdin);
//	for (int i = 0; i < 31; i++)
//		scanf("%s", maze[i]);
//	for (int i = 0; i < 31; i++)
//		printf("%s\n", maze[i]);
//	return 0;
//}

#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, casenum = 1;
	scanf("%d", &T);
	while (T--) {
		double C, F, X, now, prev = 50001.0, V = 2.0;
		scanf("%lf %lf %lf", &C, &F, &X);
		now = X / V;
		while (prev > now) {
			prev = now;
			now = prev + (C - X)/V + X/(F + V);
			V += F;
		}
		printf("Case #%d: %.7lf\n", casenum++, prev);
	}
	return 0;
}