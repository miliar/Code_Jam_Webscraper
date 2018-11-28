#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <ctime>
#include <cstring>
#include <cstdlib>
#define eps 1e-5

using namespace std;

int dp[1 << 20];
vector<double> x, y;
int n;

bool comp (double a, double b) {
	return a + eps < b;
}

int war(int state) {
	if (dp[state] != -1) return dp[state];
	int& ret = dp[state];
	ret = n;
	for (int i = 0; i < n; i++) {
		if ((state >> i) & 1) continue;
		int curr = n + 1;
		for (int j = n; j < n + n; j++) {
			if ((state >> j) & 1) continue;
			ret = min(ret, comp(y[j - n], x[i]) + war(state | 1 << i | 1 << j));
		}
	}

	return ret;
}

pair<int, int> solve(int n, vector<double>& naomi, vector<double>& ken) {
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());

	if (n == 1) {
		if (comp(naomi[0], ken[0]))
			return{ 0, 0 };
		else
		return make_pair(1, 1);
	}
	int dwar;
	dwar = 0;
	vector <double> a = naomi;
	vector <double> b = ken;
	while (!a.empty()) {
		if (a[0] + eps < b[0]) {
			a.erase(a.begin());
			b.pop_back();
		}
		else {
			dwar++;
			a.erase(a.begin());
			b.erase(b.begin());
		}
	}
	x = naomi;
	y = ken;
	::n = n;
	for (int i = 0; i <  (1 << (2 * n)); i++) dp[i] = -1;
	dp[(1 << (2 * n)) - 1] = 0;
	int War = war(0);
	return{ dwar, War };
}

int main()
{
	ifstream cin("test.in");
	ofstream cout("test.out");
	int testCount;
	int n;
	
	cin >> testCount;
	for (int testCase = 1; testCase <= testCount; testCase++) {
		cin >> n;
		vector<double> naomi(n), ken(n);
		for (int i = 0; i < n; i++) {
			cin >> naomi[i];
		}

		for (int i = 0; i < n; i++) {
			cin >> ken[i];
		}
		cout << "Case #" << testCase << ": ";
		pair<int, int> ans = solve(n, naomi, ken);
		cout << ans.first << " " << ans.second << "\n";
	}
	return 0;
}
