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
const int N = int(1e6);

inline void solve() {
	double c, f, x;
	scanf("%lf %lf %lf", &c, &f, &x);
	double ans = inf, sum = 0;
	for (int n = 0; n <= N; ++n) {
		ans = min(ans, sum + x / (2 + n * f));
		sum += c / (2 + n * f);
	}
	printf("%.7lf\n", ans);
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
