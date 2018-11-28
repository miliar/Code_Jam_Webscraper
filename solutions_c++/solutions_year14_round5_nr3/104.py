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

int q[2111];
int dp[1 << 15];
int ndp[1 << 15];

int main(){
	freopen("inputc1.in","r",stdin);
	freopen("outputc1.out","w",stdout);
	int T;
	cin >> T;
	for (int TT = 1; TT <= T; TT++){
		printf("Case #%d: ", TT);
				
		int n;
		cin >> n;
		int tot = 0;
		memset(q, 0, sizeof(q));
		for (int i = 0; i < (1 << 15); i++) dp[i] = 1;
		for (int i = 1; i <= n; i++){
			char ch;
			int e;
			cin >> ch >> e;

			int l, r;

			if (e != 0){
				if (q[e] == 0){
					q[e] = ++tot;
				}

				l = r = q[e] - 1;
			} else {
				l = 0; r = 14;
			}

			for (int mask = 0; mask < (1 << 15); mask++){
				ndp[mask] = 0;
			}

			for (int mask = 0; mask < (1 << 15); mask++){
				if (dp[mask]){
					for (int j = l; j <= r; j++){
						if (ch == 'E'){
							if ((mask & (1 << j)) == 0){
								ndp[mask ^ (1 << j)] = 1;
							}
						} else {
							if ((mask & (1 << j))){
								ndp[mask ^ (1 << j)] = 1;
							}
						}
					}
				}
			}

			for (int mask = 0; mask < (1 << 15); mask++){
				dp[mask] = ndp[mask];
			}
		}
		int ans = 100;
		for (int i = 0; i < (1 << 15); i++)
			if (dp[i]){
				int j = i;
				int x = 0;
				while (j){
					x++;
					j = (j & (j - 1));
				}
				ans = min(ans, x);
			}		
		if (ans == 100) cout << "CRIME TIME\n";
		else cout << ans << endl;
	}
    return 0;
}
