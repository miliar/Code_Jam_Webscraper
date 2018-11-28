#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

const int N = 200 + 5;
int n, k;
double p[N];
long double f[N][N];

double calcAns(vector<double> vec)
{
	memset(f, 0, sizeof f);
	f[0][0] = 1;
	for(int i = 0; i < vec.size(); ++ i) {
		for(int j = 0; j <= i; ++ j) {
			f[i + 1][j + 1] += f[i][j] * vec[i];
			f[i + 1][j] += f[i][j] * (1 - vec[i]);
		}
	}
	return f[vec.size()][vec.size() / 2];
}

void solve()
{
	cin >> n >> k;
	for(int i = 0; i < n; ++ i) {
		cin >> p[i];
	}
	sort(p, p + n);
	double ret = 0;
	for(int i = 0; i <= k; ++ i) {
		vector<double> vec;
		for(int j = 0; j < i; ++ j) vec.push_back(p[j]);
		for(int j = 0; j < k - i; ++ j) vec.push_back(p[n - 1 - j]);
		ret = max(ret, calcAns(vec));
	}
	printf("%.16f\n", (double)ret);
}

int main()
{
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
	//freopen("B-small-attempt2.in", "r", stdin); freopen("B-small-attempt2.out", "w", stdout);
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
		printf("Case #%d: ", i + 1);
		cerr << "Start: " << i << endl;
		solve();
	}
	return 0;
}
