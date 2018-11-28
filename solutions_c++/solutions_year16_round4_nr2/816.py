#include<bits/stdc++.h>
using namespace std;

double  solve() {
	int N,K;
	cin >> N >> K;
	vector<double> input(N);
	for(int i=0; i<N; i++) {
		cin >> input[i];
	}
	
	int maxA = 17;
		double  dp[maxA][maxA];
	double ans = 0.0;
	for(int bit=0; bit<(1<<N); bit++) {
		int cnt = 0;
		for(int i=0; i<N; i++)
			if((bit>>i)&1) cnt++;
		if(cnt != K) continue;
		
		for(int i=0; i<=K;i++)
			for(int j=0; j<=K/2; j++)
				dp[i][j] = 0.0;
		dp[0][0] = 1.0;
		int cur = 0;
		for(int i=0; i<N; i++)  if((bit>>i)&1) {
			int last = min(cur, K/2);
			for(int j=0; j<=last; j++) {
				dp[cur+1][j] += dp[cur][j] * (1 - input[i]);
				dp[cur+1][j+1] += dp[cur][j] * input[i];
			}
			cur++;
		}
//		cout << dp[K][K/2] << endl;
		ans = max(ans, dp[K][K/2]);
	}
	return ans;
	
}

int main() {
	int T;
	cin >> T;
	for(int _=0; _<T; _++) {
		double ans = solve();
//		cout << "Case #" << _+1 << ": " ;
		printf("Case #%d: ", _+1);
		printf("%.10lf\n", ans);
		
	}
	
	return 0;
	
}

