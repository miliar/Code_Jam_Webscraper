#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1 << 14;
int T, n, R, P, S, a[N], len, que[4][N], cnt[4];
char ch[4];

void dfs(int x, int l, int r, int q) {
	if (x == n) {
		a[l] = q;
		return;
	}
	int m = (l + r) / 2;
	if (q == 1) {
		dfs(x + 1, l, m, 1);
		dfs(x + 1, m + 1, r, 3);
	}
	if (q == 2) {
		dfs(x + 1, l, m, 2);
		dfs(x + 1, m + 1, r, 1);
	}
	if (q == 3) {
		dfs(x + 1, l, m, 3);
		dfs(x + 1, m + 1, r, 2);
	}
}

void Swap(int x1, int y1, int x2, int y2) {
	int z;
	for (int i = x1; i <= y1; i++) {
		int t = i - x1;
		int j = x2 + t;
		z = a[i];
		a[i] = a[j];
		a[j] = z;
	}
}

void sort(int x, int l, int r) {
	if (x == n) return;
	int m = (l + r) / 2;
	sort(x + 1, l, m);
	sort(x + 1, m + 1, r);
	for (int i = l; i <= m; i++) {
		int t = i - l + 1;
		int j = m + t;
		if (a[i] != a[j]) {
			if (ch[a[i]] > ch[a[j]]) {
				Swap(l , m, m + 1, r);
			}
			break;
		}
	}
}

void solve(int q) {
	que[q][0] = 0;
	dfs(1, 1, len, q);
	cnt[1] = cnt[2] = cnt[3] = 0;
	for (int i = 1; i <= len; i++) cnt[a[i]] ++;
	if (cnt[1] != R || cnt[2] != P) return;
	sort(1, 1, len);
	que[q][0] = 1;
	for (int i = 1; i <= len; i++) que[q][i] = a[i];
}

void Sort() {
	int k = 0;
	for (int i = 1; i <= 3; i++) if (que[i][0]) {
		k = i;
		break;
	}
	if (!k) {
		printf("IMPOSSIBLE");
		return;
	}
	int kk = k;
	for (int i = kk + 1; i <= 3; i++) {
		if (!que[i][0]) continue;
		for (int j = 1; j <= len; j++) {
			if (que[k][j] != que[i][j]) {
				if (que[k][j] > que[i][j]) k = i;
				break;
			}
		}
	}
	for (int i = 1; i <= len; i++) printf("%c", ch[que[k][i]]);
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &T);
	ch[1] = 'R'; ch[2] = 'P'; ch[3] = 'S';
	for (int k = 1; k <= T; k++) {
		scanf("%d %d %d %d", &n, &R, &P, &S);
		n++;
		printf("Case #%d: ", k);
		len = 1 << n - 1;
		solve(1);
		solve(2);
		solve(3);
		Sort();
		printf("\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}