#include <stdio.h>

#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int gn;
int dp[1000004];

int reverse(int n)
{
	if(n < 12)
		return n;

	int val = 0;
	while(n) {
		val = (val * 10) + (n % 10);
		n /= 10;
	}
	return val;
}

void solve(int nCase) {
	cin >> gn;

	if(gn < 21) {
		printf("Case #%d: %d\n", nCase, gn);
		return;
	}

	int n2;
	memset(dp, 0, sizeof(dp));
	for(int i=1; i<=gn; i++) {
		dp[i] = dp[i-1] + 1;
		if( (i > 20) && (i % 10) ) {
			n2 = reverse(i);
			if(n2 < i)
				dp[i] = min(dp[n2]+1, dp[i]);
		}
	}
	printf("Case #%d: %d\n", nCase, dp[gn]);
}

int main(int argc, char *argv[])
{
	// freopen("01.in", "r", stdin);

	int i, t;
	cin >> t;
	for(i=0; i<t; i++)
		solve(i+1);
	return 0;
}