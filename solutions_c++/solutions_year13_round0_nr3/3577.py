#include <cstdio>

#define N 64

int T, d[N + N], dn, t, x[N];
char s[N + N];
long long ans;

bool less(int *a, int *b, int n) {
	for (int i = n; i >= 0; --i)
		if (a[i] < b[i]) return 1;
		else if (b[i] < a[i]) return 0;
	return 0;
}

void sqrt() {
	int e[N], en = dn + 1 >> 1, sqe[N + N];
	d[dn] = 0;
	for (int i = 0; i <= dn; ++i) sqe[i] = 0;
	for (int i = 0; i <= en; ++i) e[i] = 0;
	for (int pos = en - 1; pos >= 0; --pos) {
		while (!less(d, sqe, dn)) {
			++e[pos];
			for (int i = pos; i < en; ++i)
				sqe[i + pos] += 2*e[i];
			--sqe[pos + pos];
			for (int i = pos + pos; i < dn; ++i)
				if (sqe[i] > 9) { sqe[i + 1] += sqe[i]/10; sqe[i] %= 10; }
		}
		--e[pos];
		for (int i = pos; i < en; ++i)
			sqe[i + pos] -= 2*e[i];
		--sqe[pos + pos];
		for (int i = pos + pos; i < dn; ++i)
			if (sqe[i] < 0) { sqe[i + 1] += (sqe[i] + 30)/10 - 3; sqe[i] = (sqe[i] + 30)%10; }
	}
	dn = en;
	for (int i = 0; i <= dn; ++i)
		d[i] = e[i];
}

long long recur(int a, int n, int c) {
	if (n - 1 - a < a) return 1;
	long long r = 0;
	for (int i = !a; i*i <= c; ++i) {
		x[a] = x[n - 1 - a] = i;
		if (less(d, x, dn)) break;
		r += recur(a + 1, n, c - i*i);
	}
	x[a] = x[n - 1 - a] = 0;
	return r;
}

long long solve() {
	if (dn == 0) return 0;
	sqrt();
	long long r = 0;
	for (int i = 0; i <= dn; ++i) x[i] = 0;
	for (int len = 1; len <= dn; ++len)
		r += recur(0, len, 9);
	return r;
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%s", s);
		dn = -1; while (s[++dn]);
		for (int i = 0; i < dn; ++i) d[i] = s[i] - '0';
		for (int i = 0; i + i < dn; ++i) {
			t = d[i]; d[i] = d[dn - 1 - i]; d[dn - 1 - i] = t;
		}
		--d[0];
		for (int i = 0; i < dn; ++i)
			if (d[i] < 0) {
				d[i] = 9; --d[i + 1];
			}
		if (d[dn - 1] == 0) --dn;
		ans = -solve();
		scanf("%s", s);
		dn = -1; while (s[++dn]);
		for (int i = 0; i < dn; ++i) d[i] = s[i] - '0';
		for (int i = 0; i + i < dn; ++i) {
			t = d[i]; d[i] = d[dn - 1 - i]; d[dn - 1 - i] = t;
		}
		ans += solve();
		printf("%lld\n", ans);
	}
	return 0;
}
