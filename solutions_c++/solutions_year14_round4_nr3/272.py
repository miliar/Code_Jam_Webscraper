#include <cstdio>
#include <algorithm>
using namespace std;

int sx[4] = {1, 0, -1, 0};
int sy[4] = {0, 1, 0, -1};

int a[1000][1000], tn, ti, n, m, k, i, j, x1, x2, y1, y2, from, dest, total, idx[1000][1000], xx, yy, idx_in[1000][1000], idx_out[1000][1000], ii;
int f[1000000], t[1000000], p[1000000], fl[1000000], o[1000000], ans, was[1000000], q1, q2, qu[1000000], source, vn, pr[1000000];

void paint (int x1, int y1, int x2, int y2) {
	for(int i = x1; i <= x2; i++)
		for(int j = y1; j <= y2; j++) a[i][j] = 1;
}

void addedge(int x, int y, int z) {
	t[++ii] = y; p[ii] = f[x]; f[x] = ii; fl[ii] = z; o[ii] = ii + 1;
	t[++ii] = x; p[ii] = f[y]; f[y] = ii; fl[ii] = 0; o[ii] = ii - 1;
}

bool gf () {
	for(i = 1; i <= dest; i++) was[i] = pr[i] = 0;
	q1 = q2 = 0;
	qu[q1++] = 1; was[1] = 1;
	while (q1 != q2) {
		vn = qu[q2++];
		int q = f[vn];
		while (q > 0) {
			if (!was[t[q]] && fl[q]) {
				was[t[q]] = 1;
				qu[q1++] = t[q];
				pr[t[q]] = q;
			}
			q = p[q];
		}
	}
	if (!was[dest]) return false;
	int vn = dest;
	while (vn) {
		--fl[pr[vn]];
		++fl[o[pr[vn]]];
		vn = t[o[pr[vn]]];
	}
	return true;
}

int main () {
	freopen("input.txt", "r", stdin);
	scanf("%d", &tn);
	for(ti = 1; ti <= tn; ti++) {
		scanf("%d %d %d", &n, &m, &k);
		for(i = 0; i <= m; i++) for(j = 0; j <= n; j++) a[i][j] = 0;
		for(i = 1; i <= k; i++) {
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			if (x1 > x2) swap(x1, x2);
			if (y1 > y2) swap(y1, y2);
			paint(y1, x1, y2, x2);
		}
		from = total = 1;
		dest = 2 + n * m * 2;
		ii = 0;
		for(i = 1; i <= dest; i++) f[i] = 0;
		
		for(i = 0; i < m; i++) for(j = 0; j < n; j++) {
			idx_in[i][j] = ++total;
			idx_out[i][j] = ++total;
		}
		
		for(i = m - 1; i + 1; i--) {
//			printf("line %d: ", i);
			for(j = 0; j < n; j++) {
//				putchar('0' + a[i][j]);
				if (i == 0 && a[i][j] == 0) addedge(1, idx_in[i][j], 1);
				if (i == m - 1 && a[i][j] == 0) addedge(idx_out[i][j], dest, 1);
				if (a[i][j] == 0) addedge(idx_in[i][j], idx_out[i][j], 1);
				for(k = 0; k < 4; k++) {
					xx = i + sx[k];
					yy = j + sy[k];
					if (xx < 0 || yy < 0) continue;
					if (xx > m - 1) continue;
					if (yy >= n) continue;
					if (a[xx][yy] || a[i][j]) continue;
					addedge(idx_out[i][j], idx_in[xx][yy], 1);
				}
			}
//			puts("");
		}
		ans = 0;
		while (gf()) ++ans;
		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}