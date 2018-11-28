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
const int N = 20;
const int LEN = 20;

int n, m, ans, res;
int len[N];
char s[N][LEN];
vi v[N];
int go[N * LEN][26];

inline int calc(vi &v) {
	int sz = 1;
	for (int i = 0; i < 26; ++i) {
		go[0][i] = -1;
	}
	for (int i = 0; i < sz(v); ++i) {
		int cur = 0;
		for (int j = 0; j < len[v[i]]; ++j) {
			int code = s[v[i]][j] - 'A';
			if (go[cur][code] == -1) {
				for (int z = 0; z < 26; ++z) {
					go[sz][z] = -1;
				}
				go[cur][code] = sz++;
			}
			cur = go[cur][code];
		}
	}
	return sz;
}

void gen(int x) {
	if (x >= n) {
		for (int i = 0; i < m; ++i) {
			if (sz(v[i]) == 0) {
				return;
			}
		}
		int cur = 0;
		for (int i = 0; i < m; ++i) {
			cur += calc(v[i]);
		}
		if (cur > ans) {
			ans = cur;
			res = 0;
		}
		if (cur == ans) {
			++res;
		}
		return;
	}
	for (int i = 0; i < m; ++i) {
		v[i].pb(x);
		gen(x + 1);
		v[i].pop_back();
	}
}

inline void solve() {
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; ++i) {
		scanf("%s", s[i]);
		len[i] = strlen(s[i]);
	}
	ans = 0;
	gen(0);
	printf("%d %d\n", ans, res);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
		cerr << "TEST " << i << endl;
	}
	return 0;
}
