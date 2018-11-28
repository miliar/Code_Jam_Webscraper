#include <iostream>
#include <sstream>

#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <string>
#include <deque>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>

#include <algorithm>
#include <numeric>

#define pb push_back
#define pbk pop_back
#define mp make_pair
#define fs first
#define sc second
#define all(x) (x).begin(), (x).end()
#define foreach(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define len(x) ((int) (x).size())
#define endl '\n'

#ifdef CUTEBMAING
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...) 42
#endif

using namespace std;

typedef long long int64;
typedef long double ld;
typedef unsigned long long lint;

const int inf = ((1 << 30) - 1);
const int64 linf = ((1ll << 62) - 1);
const int N = 1e4 + 100;

int n, x;
int a[N];
int dp[2][N];

inline void solve(){
	cin >> n >> x;
	for (int i = 0; i < n; i++)
		cin >> a[i];
	sort(a, a + n);
	fill_n(dp[0], n, -inf);
	dp[0][n - 1] = 0;
	int ans = 0;
	for (int i = 0; i < n; i++){
		int ci = i & 1, ni = ci ^ 1;
		fill_n(dp[ni], n, -inf);
		for (int j = n - 1; j >= i; j--){
			if (dp[ci][j] < 0)
				continue;
			ans = max(ans, dp[ci][j]);
			if (j > i)
				dp[ci][j - 1] = max(dp[ci][j - 1], dp[ci][j]);
			if (i < j && a[i] + a[j] <= x){
				dp[ni][j - 1] = max(dp[ni][j - 1], dp[ci][j] + 1);
				ans = max(ans, dp[ci][j] + 1);
			}
		}
	}
	printf("%d\n", ans + (n - ans * 2));
}

int main(){
#if defined CUTEBMAING && !defined STRESS
    assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif
	int t; cin >> t;
	for (int i = 0; i < t; i++){
		printf("Case #%d: ", i + 1);
		solve();
		eprintf("Case #%d: OK!\n", i + 1);
	}
    return 0;
}
