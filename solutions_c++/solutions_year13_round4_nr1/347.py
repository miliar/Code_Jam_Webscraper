#include <cstdio>
#include <cstring>
#include <climits>

#include <algorithm>
#include <vector>
using namespace std;

typedef long long ll;

const int MOD = 1000002013;

const int MaxM = 5555;
int n, m, r[MaxM][3];
ll f[MaxM][3];

inline int calc(int i, int j) {
	return (2LL * n - (j - i - 1)) * (j - i) / 2 % MOD;
}

int solve() {
	vector<int> p;
	int result = 0;

	scanf("%d%d", &n, &m);
	for (int i = 1; i <= m; ++ i) {
		scanf("%d%d%d", &r[i][0], &r[i][1], &r[i][2]);
		p.push_back(r[i][0]);
		p.push_back(r[i][1]);

		result = (result + (ll)calc(r[i][0], r[i][1]) * r[i][2]) % MOD;
	}

	sort(p.begin(), p.end());
	p.erase(unique(p.begin(), p.end()), p.end());
	int nn = (int)p.size() - 1;
	for (int i = 1; i <= nn; ++ i) {
		f[i][0] = p[i - 1];
		f[i][1] = p[i];
		f[i][2] = 0;
	}
	for (int i = 1; i <= m; ++ i) {
		for (int j = 1; j <= nn; ++ j) {
			if (r[i][0] <= f[j][0] && f[j][1] <= r[i][1]) {
				f[j][2] += r[i][2];
			}
		}
	}

	while (1) {
		int i = 1, j;
		ll v;
		while (i <= nn && f[i][2] == 0) ++ i;
		if (i > nn) break;
		j = i;
		v = f[i][2];
		while (j < nn && f[j + 1][2] > 0) {
			++ j;
			if (f[j][2] < v) v = f[j][2];
		}
		result = (result + MOD - (ll)calc(f[i][0], f[j][1]) * v % MOD) % MOD;
		for (int k = i; k <= j; ++ k) f[k][2] -= v;
	}
	return result;
}

int main() {
	int tn;
	scanf("%d", &tn);
	for (int t = 1; t <= tn; ++ t) {
		printf("Case #%d: %d\n", t, solve());
	}
	return 0;
}
