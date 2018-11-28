#include <bits/stdc++.h>

using namespace std;
#define limt 1010

int dp[limt][limt];
void pre()
{
	for (int i = 0; i < limt; ++i) {
	    for (int j = 0; j < i; ++j) {
	        dp[i][j] = INT_MAX;
	        for (int k = 1; k <= (i / 2); ++k) {
	            dp[i][j] = min(dp[i][j], 1 + dp[k][j] + dp[i - k][j]);
	        }
	    }
	}
}
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	pre();
	int t, n, maxi;
	int ans, fans;
	scanf("%d", &t);
	for (int kase = 1; kase <= t; ++kase) {
	    scanf("%d", &n);
	    int a[n];
	    maxi = -1;
	    for (int i = 0; i < n; ++i) {
	        scanf("%d", &a[i]);
	        maxi = max(maxi, a[i]);
	    }

	    fans = INT_MAX;
	    for (int i = 1; i <= maxi; ++i) {
	        ans = i;
	        for (int j = 0; j < n; ++j) {
	            ans += dp[a[j]][i];
	        } 
	        fans = min(fans, ans);
	    }

	    printf("Case #%d: %d\n", kase, fans);
	}

    return 0;
}

/*

*/