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
#include <climits>
#include <unordered_map>
#include <unordered_set>
using namespace std;

//#undef KVARK_DEBUG

#ifdef KVARK_DEBUG
	#include "../h/debug.h"
#else
#define dbg(...) (void(1));
#define dbg2(...) (void(1));
#define dbg3(...) (void(1));
#define dbg4(...) (void(1));
#define dbg5(...) (void(1));
#define dbgp(...) (void(1));
#define dbg_arr(...) (void(1));
#define dbg_vec(...) (void(1));
#endif

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<double, int> pdi;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<vector<int> > vvi;
typedef vector<vector<pii> > vvpii;
typedef vector<vector<long long> > vvl;
typedef vector<long long> vl;
typedef long long int llint;

#define ALL(v) (v.begin()), (v.end())
#define SZ(v) ((int)((v).size()))
#define endl "\n"

void task();

 #undef KVARK

int main(){
#ifdef KVARK
	freopen("input.txt", "r", stdin);
#else
	freopen("src/gcj_input.txt", "r", stdin);
	freopen("src/gcj_output.txt", "w", stdout);
	srand(time(0));
#endif
//	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		task();
		cout << endl;
	}

#ifdef KVARK_DEBUG
//	my_debug::printProcessInfo();
#endif
	return 0;
}
const int INF = 0x3f3f3f3f;
const int N = 3e5+10;
const int M = 3e5+10;

int n, k;
double a[210];
double dp[20][20];

void task(){
	cin >> n >> k;
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	double ans = 0;
	for (int mask = 0; mask < (1 << n); ++mask) {
		if (__builtin_popcount(mask) == k) {
			memset(dp, 0, sizeof(dp));
			vector<double> v;
			for (int i = 0; i < n; ++i)
				if ((mask & (1 << i)) > 0)
					v.push_back(a[i]);
			dp[0][0] = 1;
			for (int i = 0; i < v.size(); ++i)
				for (int mid = 0; mid <= k / 2; ++mid) {
					dp[i+1][mid+1] += dp[i][mid] * v[i];
					dp[i+1][mid] += dp[i][mid] * (1 - v[i]);
				}
			ans = max(ans, dp[v.size()][k / 2]);
		}
	}
	cout << fixed << setprecision(9) << ans;
}
