#include<iostream>
#include<string>
#include<fstream>
#include<queue>
using namespace std;
int dp[1001][1001];
int main(){
	int t;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> t;
	memset(dp, 0, sizeof dp);
	for(int i = 2; i < 1001; i++){
		for(int j = 1; j < i; j++){
			dp[i][j] = dp[i - j][j] + 1;
		}
	}
	for(int i = 0; i < t; i++){
		int d, p[1001];
		int n[1001] = {0};
		cin >> d;
		int ans = 0;
		for(int j = 0; j < d; j++){
			cin >> p[j];
			ans = max(ans, p[j]);
			n[p[j]]++;
		}
		int maxk = ans;
		for(int k = 1; k <= maxk; k++){
			int r = k;
			for(int j = k + 1; j <= maxk; j++){
				r += n[j] * dp[j][k];
			}
			ans = min(ans, r);
		}

		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0; 
}

