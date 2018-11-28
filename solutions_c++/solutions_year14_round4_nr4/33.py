#include <cstdio>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <iostream>
#include <cassert>
#include <memory.h>
using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
#define pb push_back
typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;

const int md = 1000000007;

int n, k;
string s[1010];
ll C[110][110];
int f[110][110];
ll fact[110];

pii getf(int i, int j, int q) {
	if (j - i <= k) {
		pii res(0, (C[k][j - i] * fact[j - i]) % md);
		for (int w = i; w < j; w++)
			res.first += s[w].size() - q;
		// printf("getf %d %d %d: %d, %d\n", i, j, q, res.first, res.second);
		return res;
	}

	pii res(0, 1);
	vector<pii> packs;
	bool ok = false;
	for (int w = i; w < j; ) {
		int e = w;
		while (e < j && s[e][q] == s[w][q]) e++;
		packs.pb(pii(w, e));
		if (e - w >= k) ok = true;
		w = e;
	}

	if (ok) {
		forn(w, packs.size()) {
			int S = packs[w].first;
			int F = packs[w].second;
			res.first += min(F - S, k);
			// if (s[S].size() == q + 1) S++;
			pii cur = getf(S, F, q + 1);
			res.first += cur.first;
			res.second = (ll(res.second) * cur.second) % md;
		}
	} else {
		for (int w = i; w < j; w++)
			res.first += s[w].size() - q;

		memset(f, 0, sizeof(f));
		f[0][0] = 1;
		forn(ii, packs.size())
			forn(jj, k + 1)
				if (f[ii][jj] > 0)
					forn(q, jj + 1) {
						if (q > packs[ii].second - packs[ii].first) break;
						int r = packs[ii].second - packs[ii].first - q;
						if (jj + r > k) continue;
						f[ii + 1][jj + r] = (f[ii + 1][jj + r]
							+ (((f[ii][jj] * C[jj][q] % md) * C[k - jj][r] % md) * fact[packs[ii].second - packs[ii].first] % md)
							) % md;
					}

		res.second = f[packs.size()][k];
	}

	// printf("getf %d %d %d: %d, %d\n", i, j, q, res.first, res.second);
	return res;
}

int z;

void solve() {
	scanf("%d %d", &n, &k);
	forn(i, n) {
		cin >> s[i];
		s[i] += "#";
	}

/*	z++;
	if (z == 6569) {
		printf("%d %d\n", n, k);
		forn(i, n) printf("%s\n", s[i].c_str());
	}
*/
	sort(s, s + n);

	pii ans = getf(0, n, 0);
	if (n > k) ans.first += k;
	else ans.first += n;
	ans.first -= n;
	printf("%d %d\n", ans.first, ans.second);
}

int main() {
	C[0][0] = 1;
	fact[0] = 1;
	for (int i = 1; i <= 100; i++) {
		fact[i] = fact[i-1] * i % md;
		C[i][0] = 1;
		for (int j = 1; j <= i; j++) {
			C[i][j] = C[i-1][j] + C[i-1][j-1];
			if (C[i][j] >= md) C[i][j] -= md;
		}
	}
	int tc;
	scanf("%d", &tc);
	for (int q = 1; q <= tc; q++) {
		printf("Case #%d: ", q);
		solve();
		fprintf(stderr, "Case %d done.\n", q);
	}
	return 0;
}
