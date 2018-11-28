#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <cassert>
#include <utility>
#include <iomanip>

using namespace std;

const int MAXN = 1050;
const int INF = (int) 1e9;

int tn;
int n;
int dp[MAXN][MAXN];
int a[MAXN];
int ans;

int main() {
	//assert(freopen("input.txt","r",stdin));
	//assert(freopen("output.txt","w",stdout));

	n = 1000;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			if (j == i) {
				dp[i][j] = 0;
				continue;
			}	
			dp[i][j] = INF;
			for (int k = 1; k < i; k++) {
				if (dp[k][j] + dp[i - k][j] + 1 < dp[i][j])
					dp[i][j] = dp[k][j] + dp[i - k][j] + 1;
			}
		}
	}

	scanf("%d", &tn);

	for (int test = 1; test <= tn; test++) {
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) {
			scanf("%d", &a[i]);
		}

		ans = INF;
		for (int i = 1; i <= 1000; i++) {
			int cur = 0;
			for (int j = 1; j <= n; j++) {
				cur += dp[a[j]][i];
			}
			cur += i;
			if (cur < ans)
				ans = cur;
		}

		printf("Case #%d: %d\n", test, ans);
	}

	return 0;
}