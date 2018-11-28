#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

int n;
ld V, X, r[111], c[111], res, limv[111], v[111];

const ld EPS = 1e-9;

bool special_case() {
	for (int i = 1; i <= n; i++) {
		for (int j = i+1; j <= n; j++) {
			if (c[j] < c[i]) {
				swap(r[i], r[j]);
				swap(c[i], c[j]);
			}
		}
	}
	if (c[1] > X && c[n] > X) {
		printf("IMPOSSIBLE\n");
		return true;
	}
	if (c[1] < X && c[n] < X) {
		printf("IMPOSSIBLE\n");
		return true;
	}
	if (c[1] == c[n]) {
		ld R = 0.f;
		for (int i = 1; i <= n; i++) R += r[i];
		printf("%.10Lf\n", V/R);
		return true;
	}
	return false;
}

ld calc() {
	ld ret = 0.f;
	for (int i = 1; i <= n; i++) {
		ret += c[i] * v[i];
	}
	return ret;
}

bool check(ld time) {
	for (int i = 1; i <= n; i++) limv[i] = time * r[i];
	ld usedV = 0.f;
	
	for (int i = 1; i <= n; i++) {
		ld usenow = min(V - usedV, limv[i]);
		v[i] = usenow;
		usedV += usenow;
	}
	
	if (calc() > X * V) return false;
	if (usedV < V) return false;
	
	usedV = 0.f;
	for (int i = n; i >= 1; i--) limv[i] = time * r[i];
	
	for (int i = n; i >= 1; i--) {
		ld usenow = min(V - usedV, limv[i]);
		v[i] = usenow;
		usedV += usenow;
	}
	
	if (calc() < X * V) return false;
	
	return true;
}

void bsearch() {
	ld imin = 0.f, imax = 1e15, imid;
	while (imax - imin > 0.00000000001f) {
		imid = (imin + imax) * ld(0.5f);
		if (check(imid)) imax = imid;
		else imin = imid;
	}
	res = imin;
}

void solve() {
	scanf("%d", &n);
	scanf("%Lf%Lf", &V, &X);
	for (int i = 1; i <= n; i++) {
		scanf("%Lf%Lf", &r[i], &c[i]);
	}
	if (special_case()) return;
	
	bsearch();
	printf("%.10Lf\n", res);
}

int main() {
	int T; scanf("%d", &T);
	for (int ct = 1; ct <= T; ct++) {
		printf("Case #%d: ", ct);
		solve();
	}
	return 0;
}