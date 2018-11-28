#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 30;

int n;
char x[N][N];
int y[N][N],p[N],use[N];

inline bool rec (int idx = 0) {
	if (idx == n) {
		return true;
	}

	bool in = false;
	for (int i = 0;i < n;i ++) {
		if (not use[i] and y[p[idx]][i]) {
			in = true;
			use[i] = true;

			if (not rec (idx+1)) {
				return false;
			}

			use[i] = false;
		}
	}

	return in;
}

inline int solve () {
	scanf ("%d", &n);

	for (int i = 0;i < n;i ++) {
		scanf ("%s", &x[i]);
	}

	int ans = n*n;
	for (int s = (1<<(n*n))-1;s >= 0;s --) {
		int cnt = 0;
		for (int i = 0;i < n;i ++) {
			for (int j = 0;j < n;j ++) {
				y[i][j] = x[i][j]-'0';
				if ((s>>(i*n+j))&1) {
					y[i][j] = 1;
					cnt ++;
				}
			}
			p[i] = i;
			use[i] = false;
		}

		do {
			if (not rec ()) {
				goto f;
			}
		} while (next_permutation (p, p+n));
		ans = min (ans, cnt);
		f:;
	}
	return ans;
}

int main () {
	int tt;
	scanf ("%d", &tt);

	for (int c = 1;c <= tt;c ++) {
		printf ("Case #%d: %d\n", c, solve ());
	}
}