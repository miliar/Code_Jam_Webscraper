#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>

using namespace std;

#define ll long long
#define vi vector<int>
#define pi pair<int,int>
#define pb push_back
#define mp make_pair
#define forn(i,n) for (size_t i = 0; i < n; ++i)
#define forb(i,n) for (int i = n - 1; i >= 0; --i)

const double EPS = 1e-9;
const int MAXN = 1006;
const int MOD = 1e9 + 7;
const int MOD1 = 1e9 + 35011;
const int MOD2 = 1e9 + 18169;
const int INF = (1 << 30);
const long long INFl = 1e18;

int ans, n, a[MAXN], T;

int main() {
#ifdef F0X
	freopen("input.in", "r", stdin);
	freopen("out.in", "w", stdout);
	double st = clock();
#endif

	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		ans = MOD;

		scanf("%d", &n);
		forn(i, n) scanf("%d", &a[i]);

		for (int k = 1; k < 1000; ++k) {
			int temp = 0;
			for (int i = 0; i < n; ++i) {
				temp += a[i] / k + ((a[i] % k) ? 0 : -1);
			}
			ans = min(ans, temp + k);
		}
		printf("Case #%d: %d\n", t, ans);
	}


#ifdef F0X
	cerr << "Time is " << (clock() - st) / CLOCKS_PER_SEC << endl;
#endif
	return 0;
}