//By Lin
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <bitset>
#include <cmath>
#include <string>
#include <cstdlib>
#include <vector>
#include <queue>

#define X first
#define Y second
#define mp make_pair
#define sqr(x) ((x) * (x))
#define Rep(i, n) for(int i = 0; i<(n); i++)
#define foreach(it, n) for(__typeof(n.begin()) it = n.begin(); it != n.end(); it++)

using namespace std;
typedef long long LL;
typedef pair<int, int> pii;

#define esp 1e-8
#define N 100010
#define MOD 1000000007

int n, m;
bool g[55][55];
pii target[550];
char maze[110][110];

int transfer(int x) {
	if (x <= m) return x - 1;
	x -= m;
	if (x <= n) return (m + m + 1) * x - 1;
	x -= n;
	if (x <= m) {
		x = m - x + 1;
		return (m + m + 1) * n + x - 1;
	}
	x -= m;
	x = n - x + 1;
	return (m + m + 1) * (x - 1) + m;
}

bool check() {
	memset(g, 0, sizeof g);
	Rep(i, n) Rep(j, m) {
		int a = (m + m + 1) * i + j; 
		int b = (m + m + 1) * i + m + j + 1;
		int c = (m + m + 1) * i + m + m + 1 + j;
		int d = (m + m + 1) * i + m + j;
		if (maze[i][j] == '/') g[a][d] = g[d][a] = g[b][c] = g[c][b] = 1;
		else g[a][b] = g[b][a] = g[c][d] = g[d][c] = 1;
	}
	int nn = (m + m + 1) * n + m;
	Rep(k, nn) Rep(i, nn) Rep(j, nn)
		if (g[i][k] && g[k][j]) g[i][j] = 1;
	Rep(i, n + m) {
		int x = target[i].X, y = target[i].Y;
		if (g[x][y] == 0) return false;
	}
	return true;
}
int main() {
	int cas, tt = 0;
	cin >> cas;
	while (cas --) {
		scanf("%d%d", &n, &m);
		Rep(i, n + m) {
			int x, y;
			scanf("%d%d", &x, &y);
			target[i] = mp(transfer(x), transfer(y));
//			printf("%d %d\n", target[i].X, target[i].Y);
		}
		bool flag = false;
		Rep(msk, 1 << (n * m)) {
//			msk = 3;
			Rep(i, n) Rep(j, m) {
				int t = msk & (1 << (i * m + j));
				maze[i][j] = (t == 0 ? '\\' : '/');
			}
//			Rep(i, n) Rep(j, m) printf("%c%c", maze[i][j], j == m - 1 ? '\n' : ' ');
			if (check()) {
				flag = true;
				printf("Case #%d:\n", ++tt);
				Rep(i, n) Rep(j, m) {
					printf("%c", maze[i][j]);
					if (j == m - 1) printf("\n");
				}
				break;
			}
//			break;
		}
		if (!flag) {
			printf("Case #%d:\n", ++tt);
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}
