#include <bits/stdc++.h>

using namespace std;
#define MAX 10010

int dp[MAX];

int solve(int n, int k){
	if (n <= k) return 0;
	if (dp[n] == -1){
		dp[n] = MAX;
		for (int i = 1; i < n; i++){
			dp[n] = min(dp[n], solve(n - i, k) + 1 + solve(i, k));
		}
	}
	return dp[n];
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
	int t;
	cin >> t;
	for(int ti = 0; ti < t; ti++){
		int d, temp, ans;
		cin >> d;
		vector<int> x(d);
		temp = 0;
		for (int i = 0; i < d; i++){
			cin >> x[i];
			temp = max(temp, x[i]);
		}

		ans = MAX;
		for (int i = 1; i <= temp; i++){
			int v = i;
			memset(dp, -1, temp);
			for (int j = 0; j < d; j++){
				v += solve(x[j], i);
			}
			ans = min(ans, v);
		}
		cout << "Case #" << (ti+1) << ": " << ans << '\n';
	}
	return 0;
}
