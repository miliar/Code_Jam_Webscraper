// Smile please :)

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cctype>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <iomanip>
#include <numeric>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#ifdef KVARK
	#include "debug.h"
#else
#define dbg(...) (void(1))
#define dbg2(...) (void(1))
#define dbg3(...) (void(1))
#define dbg4(...) (void(1))
#define dbg5(...) (void(1))
#define dbgp(...) (void(1))
#define dbg_arr(...) (void(1))
#define dbg_vec(...) (void(1))
#endif
#define endl "\n"

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<vector<int> > vvi;
typedef vector<vector<pii> > vvpii;
typedef vector<vector<long long> > vvll;
typedef vector<long long> vll;
typedef long long int llint;

#define all(v) (v.begin()), (v.end())

template <typename T>
inline T sqr(const T& a) {
	return a * a;
}

template <typename T>
inline int sign(const T& a) {
	return a < 0 ? -1 : a > 0;
}

void task();

int main() {
#ifdef KVARK
	freopen("input.txt", "r", stdin);
	//freopen("debug.txt", "w", stderr);
	freopen("output.txt", "w", stdout);
#else
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#endif

	task();

#ifdef KVARK
//	my_debug::printProcessInfo();
#endif
	return 0;
}

int dp[1010][1010];

void task(){
	ios_base::sync_with_stdio(0);

	for (int i = 0; i < 1010; ++i)
		for (int j = i + 1; j < 1010; ++j)
			dp[i][j] = 0;

	for (int i = 0; i < 1010; ++i)
		for (int j = 1; j < i; ++j) {
			dp[i][j] = i / j;
			for (int h = 1; h < i; ++h) {
				dp[i][j] = min(dp[i][j], dp[h][j] + dp[i - h][j] + 1);
			}
		}

	int tests;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		int ans = 0;

		int n;
		cin >> n;
		vi a(n);
		for (int i = 0; i < n; ++i)
			cin >> a[i];

		int mx = *max_element(all(a));
		ans = mx;

		for (int eat_time = mx; eat_time > 0; --eat_time) {
			int cur_ans = 0;
			for (int i = 0; i < n; ++i)
				cur_ans += dp[a[i]][eat_time];
			ans = min(ans, cur_ans + eat_time);
		}

		cout << "Case #" << test + 1 << ": ";
		cout << ans;
		cout << endl;
	}
}
