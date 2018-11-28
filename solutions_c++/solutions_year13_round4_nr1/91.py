#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

typedef long long int64;
const int MOD = 1000002013;
const int MAX_M = 1000 + 10;
int l[MAX_M], r[MAX_M], p[MAX_M];
int n, m;

int64 getCost(int64 i) {
	//n+n-1+n-2+..n-i+1
	return (n * i - i * (i - 1) / 2) % MOD;
}

void work() {

	cin >> n >> m;

	vector<int> x;

	for (int i = 0; i < m; ++i) {
		cin >> l[i] >> r[i] >> p[i];
		x.push_back(l[i]);
		x.push_back(r[i]);
	}

	sort(x.begin(), x.end());
	x.erase(unique(x.begin(), x.end()), x.end());

	vector<int64> num(x.size(), 0);

	int64 ans = 0;
	for (int i = 0; i < m; ++i) {
		ans += getCost(r[i] - l[i]) * p[i] % MOD;
		ans %= MOD;
		l[i] = lower_bound(x.begin(), x.end(), l[i]) - x.begin();
		r[i] = lower_bound(x.begin(), x.end(), r[i]) - x.begin();
		num[l[i]] += p[i];
		num[r[i]] -= p[i];
	}
	for (int i = 1; i < (int) num.size(); ++i) {
		num[i] += num[i - 1];
	}
	for (int i = 0; i + 1 < (int) x.size(); ++i) {
		//goto as right as possible!
		for (; num[i] > 0;) {
			int j;
			int64 c = num[i];
			for (j = i + 1; j + 1 < (int) x.size(); ++j) {
				if (num[j] == 0)
					break;
				c = min(c, num[j]);
			}
			ans -= getCost(x[j] - x[i]) * c % MOD;
			ans %= MOD;
			for (int k = i; k < j; ++k) {
				num[k] -= c;
			}
		}
	}
	ans %= MOD;
	if (ans < 0)
		ans += MOD;
	cout << ans << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		work();
	}
	return 0;
}
