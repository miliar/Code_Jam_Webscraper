#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#include <complex>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(s) int((s).size())
#define len(s) int((s).size())
#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...) 42
#endif
#if _WIN32 || __WIN32__
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif
#define next _next
#define prev _prev
#define rank _rank
#define hash _hash
#define y0 yy0
#define y1 yy1
#define link _link

typedef long long ll;
typedef long long llong;
typedef long long int64;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef unsigned long long ullong;
typedef unsigned long long lint;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;

const ll inf = ll(1e18);
const double eps = 1e-9;
const double pi = 4 * atan(double(1));
const int N = int(1e6) + 100;

int a[N];
ll sum[N];

inline ll get(int l, int r) {
	if (l > r) {
		return 0;
	}
	return sum[r] - (l > 0 ? sum[l - 1] : 0);
}	

inline void solve() {
	int n, p, q, r, s;
	scanf("%d %d %d %d %d", &n, &p, &q, &r, &s);
	for (int i = 0; i < n; ++i) {
		a[i] = (1LL * i * p + q) % r + s;
		sum[i] = (i > 0 ? sum[i - 1] : 0) + a[i];
	}
	double sol = 0;
	for (int i = 0; i < n; ++i) {
		ll s1 = get(0, i - 1);
		int l = i, r = n - 1;
		ll ans = inf;
		while (l <= r) {
			int mid = (l + r) / 2;
			ll s2 = get(i, mid), s3 = get(mid + 1, n - 1);
			ans = min(ans, max(s1, max(s2, s3)));
			if (s2 < s3) {
				l = mid + 1;
			} else {
				r = mid - 1;
			}
		}
		sol = max(sol, double(sum[n - 1] - ans) / sum[n - 1]);
	}
	printf("%.10lf\n", sol);
}

int main() {
	double start = clock();
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
		cerr << "Test " << i + 1 << " of " << t << endl;
		eprintf("Actual time elapsed: %.2lf\n", (clock() - start) / CLOCKS_PER_SEC);
	}
	return 0;
}
