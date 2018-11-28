#include <sstream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cassert>
#include <ctime>
#include <map>
#include <math.h>
#include <cstdio>
#include <set>
#include <deque>
#include <memory.h>
#include <queue>


using namespace std;

#pragma comment(linker, "/STACK:64000000")

typedef long long ll;

const int MAXK = 0;
const int MAXN = 1 << MAXK;
const int INF = (int)1e9;
const double EPS = 1e-9;

double f(vector<double> a) {
	int n = a.size();
	vector<vector<double> > dp(n + 1, vector<double>(n + 1, 0));
	dp[0][0] = 1;
	for (int i = 0; i < n; i++) {
		double sum = 0;
		for (int j = 0; j <= i; j++) sum += dp[i][j];
		for (int j = 0; j <= i; j++) dp[i][j] /= sum;
		for (int j = 0; j <= i; j++) {
			dp[i + 1][j] += dp[i][j] * (1 - a[i]);
			dp[i + 1][j + 1] += dp[i][j] * a[i];
		}
	}
	assert(n % 2 == 0);
	return dp[n][n / 2];
}

double slowsolve(vector<double> a, int k) {
	int n = a.size();
	double ans = 0;
	for (int mask = 0; mask < 1 << n; mask++) {
		vector<double> b;
		for (int i = 0; i < n; i++) if (mask & (1 << i)) b.push_back(a[i]);
		if (b.size() == k) {
			ans = max(ans, f(b));
		}
	}
	return ans;
}

double fastsolve(vector<double> a, int k) {
	int n = a.size();
	sort(a.begin(), a.end());
	double ans = 0;
	for (int l = 0; l <= k; l++) {
		int r = k - l;
		vector<double> b;
		for (int i = 0; i < l; i++) b.push_back(a[i]);
		for (int i = 0; i < r; i++) b.push_back(a[n - 1 - i]);
		ans = max(ans, f(b));
	}
	return ans;
}

void stress() {
	for (int it = 0;; it++) {
		cerr << it << endl;
		int n = rand() % 15 + 2;
		int k = 2 * (rand() % (n / 2) + 1);
		vector<double> a(n);
		for (int i = 0; i < n; i++) a[i] = (rand() % 101) / 100.0;
		double ans1 = fastsolve(a, k);
		double ans2 = slowsolve(a, k);
		if (fabs(ans1 - ans2) > EPS) {
			cerr << "FAIL" << endl;
			exit(0);
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	//stress();

	cerr.precision(10); cerr << fixed;
	cout.precision(10); cout << fixed;
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		cerr << "Case #" << test << ": ";
		
		int n, k;
		cin >> n >> k;
		vector<double> a(n);
		for (int i = 0; i < n; i++) cin >> a[i];

		double ans = fastsolve(a, k);
		if (n <= 16) {
			double ans2 = slowsolve(a, k);
			if (fabs(ans - ans2) > EPS) {
				cerr << "FAIL" << endl;
				assert(0);
			}
		}
		cout << ans << endl;
		cerr << ans << endl;
	}

	return 0;
}