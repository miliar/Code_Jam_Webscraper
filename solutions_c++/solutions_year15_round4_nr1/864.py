#include <stdio.h>

const int MAX=128;

int n, m;
char a[MAX][MAX];
bool u[MAX][MAX];
bool d[MAX][MAX];
bool l[MAX][MAX];
bool r[MAX][MAX];

int Test(int i, int j) {
	if (!u[i][j] && !d[i][j] && !l[i][j] && !r[i][j]) {
		return -1;
	}
	char c = a[i][j];
	if (c == '^' && !u[i][j] || c == 'v' && !d[i][j] ||
		c == '>' && !r[i][j] || c == '<' && !l[i][j])
	{
		return 1;
	}
	return 0;
}

void Solve() {
	scanf("%d%d", &n, &m);
	for (int i=0; i<n; i++) {
		scanf("%s", a[i]);
	}
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			u[i][j] = d[i][j] = l[i][j] = r[i][j] = false;
		}
	}
	for (int i=0; i<n; i++) {
		bool found = false;
		for (int j=0; j<m; j++) {
			l[i][j] = found;
			if (a[i][j] != '.') {
				found = true;
			}
		}
	}
	for (int i=0; i<n; i++) {
		bool found = false;
		for (int j=m-1; j>=0; j--) {
			r[i][j] = found;
			if (a[i][j] != '.') {
				found = true;
			}
		}
	}
	for (int j=0; j<m; j++) {
		bool found = false;
		for (int i=0; i<n; i++) {
			u[i][j] = found;
			if (a[i][j] != '.') {
				found = true;
			}
		}
	}
	for (int j=0; j<m; j++) {
		bool found = false;
		for (int i=n-1; i>=0; i--) {
			d[i][j] = found;
			if (a[i][j] != '.') {
				found = true;
			}
		}
	}
	int ans = 0;
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			if (a[i][j] != '.') {
				int res = Test(i, j);
				if (res == -1) {
					printf("IMPOSSIBLE\n");
					return;
				}
				ans += res;
			}
		}
	}
	printf("%d\n", ans);
}

int main() {
	int nt;
	scanf("%d", &nt);
	for (int i=1; i<=nt; i++) {
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
