#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 20;
const int MOD = 10000007;
int dp[1 << N];
int main () {
	freopen ("input.txt" , "r" , stdin);
	freopen ("output.txt" , "w" , stdout);
	int t , cas = 0;scanf ("%d" , &t);
	while (t --) {
		int r , c , w;
		scanf ("%d %d %d" , &r , &c , &w);
		int ans = c / w;
		if (c % w == 0) ans += w - 1;
		else {
			ans += w;
		}
		
		printf ("Case #%d: %d\n" , ++ cas , ans + (r - 1) * (c / w));
	}
	return 0;
}