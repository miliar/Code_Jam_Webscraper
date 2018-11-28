#include <cstdio>
#include <algorithm>
using namespace std;

const int Maxn = 105;

int T;
int n, m;
int R[Maxn], C[Maxn];
char B[Maxn][Maxn];

bool checkRow(int r, int c1, int c2)
{
	for (int j = c1; j <= c2; j++)
		if (B[r][j] != '.') return true;
	return false;
}

bool checkCol(int c, int r1, int r2)
{
	for (int i = r1; i <= r2; i++)
		if (B[i][c] != '.') return true;
	return false;
}

int main()
{
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d %d", &n, &m);
		fill(R, R + n, 0); fill(C, C + m, 0);
		for (int i = 0; i < n; i++) {
			scanf("%s", B[i]);
			for (int j = 0; j < m; j++)
				if (B[i][j] != '.') { R[i]++; C[j]++; }
		}
		printf("Case #%d: ", tc);
		bool ok = true;
		int res = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (B[i][j] != '.')
					if (R[i] == 1 && C[j] == 1) ok = false;
					else if (B[i][j] == '<' && !checkRow(i, 0, j - 1) ||
						     B[i][j] == '>' && !checkRow(i, j + 1, m - 1) ||
						     B[i][j] == '^' && !checkCol(j, 0, i - 1) ||
						     B[i][j] == 'v' && !checkCol(j, i + 1, n - 1))
						res++;
		if (ok) printf("%d\n", res);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}