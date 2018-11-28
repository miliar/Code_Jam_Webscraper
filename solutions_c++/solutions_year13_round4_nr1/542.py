#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;

const int MAXM = 5000;
const long long mo = 1000002013LL;

struct tdot {
	int x, y;
	tdot(int x_, int y_) {
		x = x_; y = y_;
	}
	tdot() {}
}	d[MAXM];

int cmp(tdot a, tdot b) {
	return a.x < b.x;
}

int n, m, a[MAXM], b[MAXM], c[MAXM];
long long cnt[MAXM], e[MAXM], origin[MAXM];

long long calc(long long len) {
	// cout << len << ' ' << (2 * n - len + 1) * len / 2 << endl;
	return (2 * n - len + 1) * len / 2;
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T, TT = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &n, &m);
		long long oans = 0;
		for (int i = 0; i < m; i++) {
			scanf("%d%d%d", &a[i], &b[i], &c[i]);
			oans = (oans + (calc(b[i] - a[i]) % mo) * c[i] % mo) % mo;
			d[i * 2] = tdot(a[i], i * 2);
			d[i * 2 + 1] = tdot(b[i], i * 2 + 1);
		}
		// cout << oans << endl;
		sort(d, d + 2 * m, cmp); 
		e[d[0].y] = 1; origin[e[d[0].y]] = d[0].x;
		for (int i = 1; i < 2 * m; i++) {
			e[d[i].y] = e[d[i - 1].y] + (d[i].x != d[i - 1].x);
			origin[e[d[i].y]] = d[i].x;
		}
		//for (int i = 0; i < 2 * m; i++) cout << e[i] << ' '; cout << endl;
		int o = e[d[2 * m - 1].y];
		for (int i = 0; i < m; i++) a[i] = e[i * 2];
		for (int i = 0; i < m; i++) b[i] = e[i * 2 + 1];
		//for (int i = 0; i < m; i++) cout << a[i] << ' ' << b[i] << endl;
		// for (int i = 1; i <= o; i++) cout << origin[i] << endl;
		//cout << "--------- " << o << endl;
		memset(cnt, 0, sizeof(cnt));
		for (int i = 0; i < m; i++)
			for (int j = a[i]; j < b[i]; j++) 
				cnt[j] += c[i];
		// for (int i = 1; i <= o; i++) cout << cnt[i] << endl;
		long long ans = 0;
		for (int i = 0; i < o; i++) {
			long long f = -1, k = -1;
			for (int j = 1; j <= o; j++) if (cnt[j] > 0 && (f == -1 || cnt[j] < f)) {
				f = cnt[j]; k = j;
			}
			if (k == -1) break;
			int l = k, r = k;
			while (l > 1 && cnt[l - 1] > 0) l--;
			while (r < o && cnt[r + 1] > 0) r++;
			// cout << l << ' ' << r << ' ' << k << ' ' << f << endl;
			ans = (ans + (f % mo) * calc(origin[r + 1] - origin[l]) % mo) % mo;
			for (int j = l; j <= r; j++) cnt[j] -= f;
		}
		cout << "Case #" << ++TT << ": " << (oans - ans + mo) % mo << endl;
	}
	return 0;
}
