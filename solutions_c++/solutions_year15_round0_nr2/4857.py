#include <iostream>
#include <vector>
using namespace std;
#define MAX 10010

int dp[MAX];

int solve(int n, int k){
	if (n <= k) return 0;
	if (dp[n] == -1){
		dp[n] = MAX;
		for (int i = 1; i < n; i++){
			dp[n] = min(dp[n], solve(n-i, k) + solve(i, k) + 1);
		}
	}
	return dp[n];
}

int main() {
	int t, cases = 1;
	cin >> t;
	
	
	while (t--){
		int d;
		vector<int> x;
		cin >> d;
		x.resize(d);
		int sz = 0;
		for (int i = 0; i < d; i++){
			cin >> x[i];
			sz = max(sz, x[i]);
		}
		
		
		int ans = MAX;
		for (int i = 1; i <= sz; i++){
			int v = i;
			fill(dp, dp+sz+1, -1);
			for (int j = 0; j < d; j++){
				v += solve(x[j], i);
			}
			ans = min(ans, v);
			cout << "i: " << i << " v: " << v << endl;
		}
		cout << "Case #" << cases++ << ": " << ans << endl;
	}
	return 0;
}