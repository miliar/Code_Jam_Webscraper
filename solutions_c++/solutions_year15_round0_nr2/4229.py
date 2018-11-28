// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

const int MAXP = 1010;

int getans(int P, int L, vector<vector<int>>& dp){
	if (dp[P][L] != -1)
		return dp[P][L];
	if (L >= P) return 0;
	int ans = P + 100;
	for (int i = 1; i <= P - 1; i++){
		ans = min(ans, getans(P - i, L, dp) + getans(i, L, dp) + 1);
	}
	dp[P][L] = ans;
	return ans;
}

int main(){
	vector<vector<int>> dp(MAXP, vector<int>(MAXP, -1));
	int T;
	cin >> T;
	for (int tt = 0; tt < T; tt++){
		int D;
		cin >> D;
		vector<int> pi(D);
		for (int dd = 0; dd < D; dd++){
			cin >> pi[dd];
		}
		int maxpi = *max_element(pi.begin(), pi.end());
		int ans = maxpi;
		for (int i = 1; i < maxpi; i++){
			int res = i;
			for (int j = 0; j < D; j++)
				res += getans(pi[j], i,dp);
			ans = min(ans, res);
		}
		cout << "Case #" << tt + 1 << ": " << ans << endl;
	}
}


