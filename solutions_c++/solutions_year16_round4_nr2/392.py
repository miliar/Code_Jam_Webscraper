#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <string>

using namespace std;

typedef long long i64;

double get_ans(const vector <double> &arr) {
	int k = arr.size();
	vector <vector <double> > ans(k + 1, vector <double>(k + 1, 0));
	ans[0][0] = 1;
	for (int i = 0; i < k; i++) {
		auto cur = ans;
		for (int x = 0; x <= k / 2; x++)
			for (int y = 0; y <= k / 2; y++) {
				cur[x + 1][y] += ans[x][y] * arr[i];
				cur[x][y + 1] += ans[x][y] * (1 - arr[i]);
			}
		ans = cur;
	}
	return ans[k / 2][k / 2];
}

void dummy(int n, int k, const vector <double> &arr) {
	double ans = 0;
	vector <double> res(k);
	vector <double > vans;
	for (int mask = 0; mask < (1 << n); mask++) {
		res.clear();
		for (int j = 0; j < n; j++)
			if (mask & (1 << j))
				res.push_back(arr[j]);
		if (res.size() != k)
			continue;
		double cur = get_ans(res);
		if (cur > ans) {
			ans = cur;
			vans = res;
		}
	}
	printf("%.9lf\n", ans);
	for (int i = 0; i < k; i++)
		cout << vans[i] << " ";
	cout << endl;
}

void tyc(int t, int n, int k, vector <double> arr) {
	sort(arr.begin(), arr.end());
	double ans = 0;
	for (int i = 0; i <= k; i++) {
		vector <double> cur;
		for (int j = 0; j < i; j++)
			cur.push_back(arr[j]);
		int idx = n - 1;
		while (cur.size() != k) {
			cur.push_back(arr[idx--]);
		}
		ans = max(ans, get_ans(cur));
	}
	printf("Case #%d: %.9lf\n", t, ans);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; t++) {
		int n, k;
		cin >> n >> k;
		vector <double> arr(n);
		for (int i = 0; i < n; i++)
			cin >> arr[i];
		//dummy(n, k, arr);
		tyc(t, n, k, arr);
	}
}
