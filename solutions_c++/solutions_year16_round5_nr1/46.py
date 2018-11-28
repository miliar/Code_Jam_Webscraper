#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int dp[N][2], dp2[N][2];

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		string s;
		cin >> s;
		for (int i = 0; i <= s.size(); i++) for (int j = 0; j < 2; j++) dp[i][j] = -1e9 + 1;
		dp[0][0] = dp[0][1] = 0;

		for (int it = 0; it < s.size(); it++) {
			for (int i = 0; i <= it + 1; i++) for (int j = 0; j < 2; j++) dp2[i][j] = -1e9 + 1;
			int t = 0;
			if (s[it] == 'J') t = 1;

			for (int i = 0; i <= it + 1; i++) for (int j = 0; j < 2; j++) if (dp[i][j] >= 0) {
				if (i > 0) {
					if (t == j) {
						dp2[i - 1][j ^ 1] = max(dp2[i - 1][j ^ 1], dp[i][j] + 10);
					} else {
						dp2[i - 1][j ^ 1] = max(dp2[i - 1][j ^ 1], dp[i][j] + 5);
					}
				}
				if (i == 0 || j != t) dp2[i + 1][t] = max(dp2[i + 1][t], dp[i][j]);
			}
			for (int i = 0; i <= it + 1; i++) for (int j = 0; j < 2; j++) dp[i][j] = dp2[i][j];
		}
		cout << "Case #" << tt << ": ";

		int ans = max(dp[0][0], dp[0][1]);
		cout << ans << endl;


	}
	return 0;
}