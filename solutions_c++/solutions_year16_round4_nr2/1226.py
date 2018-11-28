#pragma comment(linker, "/STACK:134217728") //128mb
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <cassert>
#include <climits>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <cmath>
#include <set>
#include <map>
#include <hash_set>
#include <hash_map>
#include <algorithm>
#include <random>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <complex>
using namespace std;


#define input_txt freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout)
#define in_out(x) freopen(x".in", "r", stdin);freopen(x".out", "w", stdout)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(s) int((s).size())
#define all(x) x.begin(),x.end()

typedef long long ll;
typedef long long llong;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef complex<double> comp;

const long long MOD = 1000000000 + 7; //1e9+7
const long long MAGIC = 123123123;
const double PI = 4 * atan(1.);
const double EPS = 1E-7;



struct cmp_for_set {
	bool operator()(const int & a, const int & b){ return a > b; }
};

void time_elapsed() { cout << "\nTIME ELAPSED: " << (double)clock() / CLOCKS_PER_SEC << " sec\n"; }
#define DOUT_VAR(x) cout << #x << " = " << (x) << endl
template<typename T> void DOUT_VEC(vector<T> & vec) { puts("");  for (auto i : vec) cout << i << " "; puts(""); }
template<typename T> void DOUT_TABLE(vector<vector<T>> & vec) { puts(""); for (auto i : vec) { for (auto j : i) cout << j << " "; cout << endl; }puts(""); }

template<typename T> T gcd(T a, T b){ return ((!b) ? a : gcd(b, a%b)); }
template<typename T>T gcd(T a, T b, T&x, T&y){ if (!a){ x = 0, y = 1; return b; }T x1, y1; T d = gcd(b%a, a, x1, y1); x = y1 - (b / a)*x1; y = x1; return d; }

template<typename T> T lcm(T a, T b) { return (a / gcd(a, b))*b; }
template<typename T, typename M> T neg_mod(T a, M mod) { return ((a%mod) + mod) % mod; }
ll binpow(ll x, ll p) { ll res = 1; while (p){ if (p & 1) res *= x; x *= x; p >>= 1; }return res; }
ll binpow_mod(ll x, ll p, ll m) { ll res = 1; while (p){ if (p & 1) res = (res*x) % m; x = (x*x) % m; p >>= 1; }return res; }


double dp[202][202][202];
int n, k;
double p[202];

int bit_cnt(int mask) {
	int res = 0;
	while (mask > 0) {
		res += ((mask & 1) > 0);
		mask >>= 1;
	}
	return res;
}

double solve() {
	for (int i = 0; i <= n; ++i) {
		for (int j = 0; j <= k; ++j) {
			for (int jj = 0; jj <= k; ++jj) {
				dp[i][j][jj] = 0;
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		dp[i][0][0] = 1;
	}

	dp[0][1][1] = p[0];
	dp[0][1][0] = 1 - p[0];
	for (int i = 1; i < n; ++i) {
		for (int j = 1; j <= k; ++j) {
			for (int m = 0; m <= j; ++m) {
				dp[i][j][m] = dp[i - 1][j][m];
				double rel;
				if (m>0) {
					rel = p[i] * dp[i - 1][j - 1][m - 1];
					dp[i][j][m] = max(dp[i][j][m], rel);
				}
				rel = (1 - p[i])*dp[i - 1][j - 1][m];
				dp[i][j][m] = max(dp[i][j][m], rel);
			}
		}
	}
	
	return dp[n-1][k][k / 2];
}

double solve_slow() {
	double res = 0;
	for (int mask = 0; mask < (1 << n); ++mask) {
		if (bit_cnt(mask) != k) continue;
		vector<int>vec;
		for (int i = 0; i < n; ++i) {
			if (mask&(1 << i)) vec.push_back(i);
		}

		vector<vector<double>>prob(n, vector<double>(n + 1));
		prob[0][0] = (1 - p[vec[0]]);
		prob[0][1] = p[vec[0]];
		for (int i =1; i < k; ++i) {
			for (int j = 0; j <= k; ++j) {
				prob[i][j] = prob[i - 1][j] * (1 - p[vec[i]]);
				if (j) prob[i][j] += prob[i - 1][j - 1]*p[vec[i]];
			}
		}
		res = max(res, prob[k - 1][k / 2]);
	}
	return res;
}

int main() {
	input_txt;

	int tests_cnt;
	cin >> tests_cnt;
	for (int T = 1; T <= tests_cnt; ++T) {
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; ++i) {
			scanf("%lf", &p[i]);
		}

		printf("Case #%d: ", T);
		printf("%.8lf\n", solve_slow());
	}


	//time_elapsed();
	return 0;
}