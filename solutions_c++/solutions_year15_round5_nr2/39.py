#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <map>
#include <cassert>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const int MAXN = 1010;
const int MAXK = 110;

int n, k;
int s[MAXN];
int l[MAXK], r[MAXK];

int a[MAXK], b[MAXK];

bool dp[MAXK][MAXK];

bool good(int d) {
	forn(i, k) {
		a[i] = -l[i];
		b[i] = d - r[i];

		if (a[i] > b[i])
			break;
	}

	memset(dp, 0, sizeof(dp));
	dp[0][0] = true;

	forn(i, k)
		forn(j, k)
			if (dp[i][j]) {
				int q = (a[i] + ((ll)1e9) * k) % k;
				forab(z, a[i], min(a[i] + k, b[i] + 1)) {
					dp[i + 1][(j + q) % k] = true;
					q = (q + 1) % k;
				}
			}

	int v = (s[0] + ((ll)1e9) * k) % k;

	return dp[k][v];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d ", &T);

	forn(test, T) {
		cerr << test << '\n';

		printf("Case #%d: ", test + 1);

		scanf("%d%d", &n, &k);
		
		forn(i, n - k + 1)
			scanf("%d", &s[i]);

		forn(i, k) {
			l[i] = r[i] = 0;
			int cur = 0;
			for(int j = i; j + 1 < n - k + 1; j += k) {
				cur += s[j + 1] - s[j];
				l[i] = min(l[i], cur);
				r[i] = max(r[i], cur);
			}
		}

		int L = -1, R = 1e9;
		while (R - L > 1) {
			int M = (L + R) / 2;
			if (good(M))
				R = M;
			else
				L = M;
		}

		printf("%d\n", R);
	}
	return 0;
}
