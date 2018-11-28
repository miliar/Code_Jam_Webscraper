#include <cstdio>
#include <cstring>

const int maxn = 100;

bool ans;
int casei, cases, n, m, maxr;
int maxc[maxn];
int board[maxn][maxn];
int check[maxn][maxn];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j) 
				scanf("%d", board[i] + j);
				
		memset(check, 0, sizeof check);
		
		memset(maxc, 0, sizeof maxc);
		for (int i = 0; i < n; ++i) {
			maxr = 0;
			for (int j = 0; j < m; ++j) {
				if (maxr > board[i][j]) check[i][j] |= 1;
				else maxr = board[i][j];
				if (maxc[j] > board[i][j]) check[i][j] |= 2;
				else maxc[j] = board[i][j];
			}
		}
		
		memset(maxc, 0, sizeof maxc);
		for (int i = n - 1; i >= 0; --i) {
			maxr = 0;
			for (int j = m - 1; j >= 0; --j) {
				if (maxr > board[i][j]) check[i][j] |= 4;
				else maxr = board[i][j];
				if (maxc[j] > board[i][j]) check[i][j] |= 8;
				else maxc[j] = board[i][j];
			}
		}
		
		ans = true;
		for (int i = 0; i < n && ans; ++i)
			for (int j = 0; j < m && ans; ++j) 
				if ((check[i][j] & 5) && (check[i][j] & 10)) ans = false;
				
		if (ans) printf("Case #%d: YES\n", casei);
		else printf("Case #%d: NO\n", casei);
	}

	return 0;
}
