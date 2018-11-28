#include <cstdio>
#include <algorithm>
using namespace std;

const int Maxn = 105;

int t;
int n, m;
int A[Maxn][Maxn];
int R[Maxn], C[Maxn];

bool Pos()
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (min(R[i], C[j]) != A[i][j]) return false;
	return true;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d", &n, &m);
		fill(R, R + n, 0); fill(C, C + m, 0);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) {
				scanf("%d", &A[i][j]);
				R[i] = max(R[i], A[i][j]); C[j] = max(C[j], A[i][j]);
			}
		printf("Case #%d: %s\n", tc, Pos()? "YES": "NO");
	}
	return 0;
}