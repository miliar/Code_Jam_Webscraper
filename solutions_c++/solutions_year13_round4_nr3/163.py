#include <cstdio>
#include <algorithm>
using namespace std;

const int Maxn = 22;

int t;
int n;
int a[Maxn], b[Maxn];
bool mat[Maxn][Maxn];
int res[Maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		for (int i = 0; i < n; i++)
			scanf("%d", &b[i]);
		fill((bool*)mat, (bool*)mat + Maxn * Maxn, false);
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				if (a[i] >= a[j]) mat[i][j] = true;
				else if (b[i] <= b[j]) mat[j][i] = true;
		for (int k = 0; k < n; k++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					mat[i][j] |= mat[i][k] && mat[k][j];
        for (int i = 0; i < n; i++) if (a[i] > 1) {
            int j = i - 1;
            while (a[j] + 1 != a[i]) j--;
            mat[i][j] = true;
        }
        for (int i = n - 1; i >= 0; i--) if (b[i] > 1) {
            int j = i + 1;
            while (b[i] != b[j] + 1) j++;
            mat[i][j] = true;
        }
		printf("Case #%d:", tc);
		fill(res, res + n, 0);
		for (int i = 1; i <= n; i++) {
			int j;
			for (j = 0; j < n; j++) if (!res[j]) {
				int l;
				for (l = 0; l < n; l++)
					if (!res[l] && mat[j][l]) break;
				if (l == n) break;
			}
			res[j] = i;
		}
		for (int i = 0; i < n; i++)
			printf(" %d", res[i]);
		printf("\n");
	}
	return 0;
}
