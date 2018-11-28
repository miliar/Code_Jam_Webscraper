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

const double inf = 1e100;
const double eps = 1e-9;
const double pi = 4 * atan(double(1));
const int N = 2222;

int n;
char buf[111];
int a[N], b[N];
int d[N][N];
bool used[N][N];

inline int nextInt() {
	scanf("%s", buf);
	int len = strlen(buf), ptr = 0;
	while (buf[ptr] != '.') {
		++ptr;
	}
	++ptr;
	int res = 0, added = 0;
	while (ptr < len) {
		++added;
		res = res * 10 + buf[ptr++] - '0';
	} 
	while (added < 6) {
		res *= 10;
		++added;
	}
	return res;
}

int calc(int mask1, int mask2) {
	if (mask1 == 0) {
		return 0;
	}
	if (used[mask1][mask2]) {
		return d[mask1][mask2];
	}
	used[mask1][mask2] = true;
	int maxB = -1;
	for (int i = 0; i < n; ++i) {
		if ((mask2 & (1 << i)) != 0) {
			maxB = max(maxB, b[i]);
		}
	}
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		if ((mask1 & (1 << i)) != 0) {
			if (maxB > a[i]) {
				for (int j = 0; j < n; ++j) {
					if ((mask2 & (1 << j)) != 0 && b[j] > a[i]) {
						ans = max(ans, calc((mask1 ^ (1 << i)), (mask2 ^ (1 << j))));
					}
				}
			}
			else {
				for (int j = 0; j < n; ++j) {
					if ((mask2 & (1 << j)) != 0 && b[j] < a[i]) {
						ans = max(ans, calc((mask1 ^ (1 << i)), (mask2 ^ (1 << j))) + 1);
						//break;
					}
				}
			}
		}
	}
	return d[mask1][mask2] = ans;
}


int calc2(int mask1, int mask2) {
	if (mask1 == 0) {
		return 0;
	}
	if (used[mask1][mask2]) {
		return d[mask1][mask2];
	}
	used[mask1][mask2] = true;
	int maxB = -1;
	for (int i = 0; i < n; ++i) {
		if ((mask2 & (1 << i)) != 0) {
			maxB = max(maxB, b[i]);
		}
	}
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		if ((mask1 & (1 << i)) != 0) {
			if (maxB > a[i]) {
				for (int j = 0; j < n; ++j) {
					if ((mask2 & (1 << j)) != 0 && b[j] > a[i]) {
						ans = max(ans, calc2((mask1 ^ (1 << i)), (mask2 ^ (1 << j))));
						break;
					}
				}
			}
			else {
				for (int j = 0; j < n; ++j) {
					if ((mask2 & (1 << j)) != 0 && b[j] < a[i]) {
						ans = max(ans, calc2((mask1 ^ (1 << i)), (mask2 ^ (1 << j))) + 1);
						break;
					}
				}
			}
		}
	}
	return d[mask1][mask2] = ans;
}

inline void solve() {
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)	 {
		a[i] = nextInt();
	}
	for (int i = 0; i < n; ++i) {
		b[i] = nextInt();
	}
	sort(a, a + n);
	sort(b, b + n);
	memset(used, false, sizeof(used));
	int ans = calc((1 << n) - 1, (1 << n) - 1);
	memset(used, false, sizeof(used));
	int ans2 = calc2((1 << n) - 1, (1 << n) - 1);
	
	cout << ans << " " << ans2 << endl;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
