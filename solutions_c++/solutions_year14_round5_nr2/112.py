#include <iostream>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <vector>
#include <cstring>
#include <cstdlib>

#define mp make_pair
#define pb push_back
#define ppb pop_back
#define X first
#define Y second

using namespace std;

int p[200], q[200];

int dp[200][2111];

int main(){
	freopen("inputb2.in","r",stdin);
	freopen("outputb2.out","w",stdout);
	int T;
	cin >> T;
	for (int TT = 1; TT <= T; TT++){
		printf("Case #%d: ", TT);
				
		int P, Q, n;
		cin >> P >> Q >> n;
		for (int i = 1; i <= n; i++) cin >> p[i] >> q[i];

		for (int i = 0; i <= n; i++){
			for (int j = 0; j <= 2000; j++) dp[i][j] = -1000000000;
		}

		dp[0][1] = 0;
		dp[0][0] = 0;

		for (int i = 0; i <= n; i++){
			int M = dp[i][2000];
			for (int j = 2000; j >= 0; j--){
				M = max(M, dp[i][j]);
				dp[i][j] = max(dp[i][j], M);
			}

			if (i == n) break;

			for (int j = 0; j <= 2000; j++){
				dp[i + 1][j + (p[i + 1] + Q - 1) / Q] = max(dp[i + 1][j + (p[i + 1] + Q - 1) / Q], dp[i][j]);
				for (int p1 = 1; p1 <= 10; p1++){
					for (int p2 = 0; p2 <= 10; p2++){
						if (p1 * P + p2 * Q >= p[i + 1]){
							if ((p1 - 1) * P + p2 * Q < p[i + 1]){
								if (j - (p1 - 1) + p2 > 0){
									dp[i + 1][j - p1 + p2] = max(dp[i + 1][j - p1 + p2], dp[i][j] + q[i + 1]);
								}
							} else
							break;
						}
					}
				}
			}
		}
		cout << dp[n][0] << endl;
	}
    return 0;
}
