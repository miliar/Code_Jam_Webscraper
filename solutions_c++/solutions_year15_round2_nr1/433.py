#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define pb push_back
#define mp make_pair
int dp[1000005];
int rev(int i) {
	int k = 0;
	while (i > 0) {
		k *= 10;
		k += i % 10;
		i /= 10;
	}
	return k;
}
int main() {
	int tc;
	cin >> tc;
	for (int i = 0; i <= 1000002; i++) {
		if (dp[i+1] == 0)
			dp[i+1] = dp[i] + 1;
		else
			dp[i+1] = min(dp[i] + 1, dp[i + 1]);
		
		if (rev(i) < 1000005 && dp[rev(i)] == 0)
			dp[rev(i)] = 1 + dp[i];
		else if (rev(i) < 1000005)
			dp[rev(i)] = min(dp[rev(i)], 1 + dp[i] + 1);
	}
	for (int t = 0; t < tc; t++) {
		int n;
		cin >> n;
		
		cout << "Case #" << t+1 << ": " << dp[n] << endl;
	}
	return 0;
}
