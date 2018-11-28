#include <bits/stdc++.h>

using namespace std;

void doCase(int t) {
	string mood;
	cin >> mood;
	
	int N = mood.size();
	
	vector<vector<int>> dp(N, vector<int>(N+1));
	
	for (int i=0; i<N; i++) {
		dp[i][i] = 0;
	}
	
	for (int len=2; len<=N; len+=2) {
		for (int i=0; i+len<=N; i++) {
			dp[i][i+len] = dp[i+1][i+len-1] + 1;
			if (mood[i] == mood[i+len-1]) dp[i][i+len]+=1;
			for (int part = 2; part < len; part += 2) {
				dp[i][i+len] = max(dp[i][i+len], dp[i][i+part] + dp[i+part][i+len]);
			}
		}
	}
	
	cout << "Case #" << t << ": " << 5*dp[0][N] << endl;
}

int main() {
	int T;
	cin>> T;
	for (int i=1; i<=T; i++) doCase(i);
	return 0;
}
