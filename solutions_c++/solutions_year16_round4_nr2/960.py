#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int N, K;
		double res = 0.0;
		vector<double> P;
		cin >> N >> K;
		P.resize(N);
		for(int i = 0; i < N; i++)
			cin >> P[i];
		sort(P.begin(), P.end());
		for(int k = 0; k <= K; k++) {
			vector<double> use;
			for(int i = 0; i < k; i++) {
				use.push_back(P[i]);
			}
			for(int i = 0; i < K-k; i++) {
				use.push_back(P[N-1 -i]);
			}
			double dp[300] = {};
			dp[0] = 1.0;
			for(int i = 0; i < use.size(); i++) {
				double tmp[300] = {};
				for(int j = 0; j < 250; j++) {
					tmp[j+1] += dp[j] * use[i];
					tmp[j]   += dp[j] * (1.0 - use[i]);
				}
				for(int j = 0; j < 300; j++) {
					dp[j] = tmp[j];
				} 
			}
			res = max(res,dp[K/2]);
		}
		printf("Case #%d: %.10f\n", t, res);
	}
}
