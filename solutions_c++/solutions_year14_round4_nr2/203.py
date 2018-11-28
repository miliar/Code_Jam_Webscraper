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

const int inf = int(1e9);
const double eps = 1e-9;
const double pi = 4 * atan(double(1));
const int N = 1010;

int a[N];

inline int calc(vi v) {
	int ans = 0;
	for (int i = 0; i < sz(v); ++i) {
		for (int j = i + 1; j < sz(v); ++j) {
			if (v[i] > v[j]) {
				++ans;
			}
		}
	}
	return ans;
}

void solve() {
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
	}
	int pos = 0;
	for (int i = 1; i < n; ++i) {
		if (a[i] > a[pos]) {
			pos = i;
		}
	}
	int ans = inf;
	for (int i = 1; i < (1 << n); ++i) {
		if ((i & (1 << pos)) == 0) {
			continue;
		}
		int res = 0, ptr = 0;
		vi v1, v2;
		for (int j = 0; j < n; ++j) {
			if ((i & (1 << j)) != 0) {
				v1.pb(a[j]);
				res += j - ptr++;
			} else {
				v2.pb(a[j]);
			}
		}
		reverse(v2.begin(), v2.end());
		res += calc(v1) + calc(v2);
		ans = min(ans, res);
		if (res == 6) {
			for (int j = 0; j < sz(v1); ++j) {
				cerr << v1[j] << " ";
			}
			cerr << endl;
		}	
	}
	cout << ans << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}
	return 0;
}
