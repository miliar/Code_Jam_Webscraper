#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long lld;

lld low[12345], at[12345];
lld v[12345];
lld e, r;
int n;

lld regen;
lld solve(int l, int r) {
	if (l==r) return 0;
	int bi = l;
	for (int i=l; i<r; i++) {
		if (v[i] > v[bi]) {
			bi = i;
		}
	}
	lld sum = 0;
	lld use = at[bi] - low[bi];
	sum += v[bi] * use;
	low[bi] = at[bi];
	for (int i=bi-1; i>=l; i--) {
		low[i] = max(low[i+1]-regen, (lld)0);
	}
	at[bi] -= use;
	for (int i=bi+1; i<r; i++) {
		at[i] = min(at[i-1]+regen, e);
	}
	sum += solve(l, bi);
	sum += solve(bi+1, r);
	return sum;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ti=0; ti<t; ti++) {
		scanf("%lld%lld%d", &e, &r, &n);
		regen = r;
		for (int i=0; i<n; i++) {
			low[i] = 0;
			at[i] = e;
			scanf("%lld", &v[i]);
		}
		lld ret = solve(0, n);
		printf("Case #%d: %lld\n", ti+1, ret);
	}
	return 0;
}