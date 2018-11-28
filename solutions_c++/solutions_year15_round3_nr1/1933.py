#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int R, C, W;
int dp[1<<22]; // 0 - unknown, 1 - hit, 2 - miss
#define bit(x, n) ((x>>(2*n))&3)

bool verify(int status) {
	for(int i = 0; i + W <= C; ++i) {
		bool ok = true;
		for(int j = 0; j < C; ++j) {
			int b = bit(status, j);
			if(b == 0) continue;
			if(b == 1 && (j < i || j >= i + W) || b == 2 && j >= i && j < i + W) {
				ok = false;
				break;
			}
		}
		if(ok) return true;
	}
	return false;
}

void show(int status) {
	for(int i = 0; i < C; ++i) {
		int b = bit(status, i);
		printf("%d ", b);
	}
}

void dfs(int status) {
	if(dp[status] != -1) return;
	if(verify(status) == false) {
		dp[status] = -2;
		return;
	}
	dp[status] = 1000000;
	int cnt = 0;
	for(int i = 0; i < C; ++i) {
		int b = bit(status, i);
		if(b == 1) ++cnt;
	}
	if(cnt == W)
		dp[status] = 0;
	else for(int i = 0; i < C; ++i) {
		if(bit(status, i) != 0) continue;
		int tmp = -1;
		dfs(status | (1 <<(2*i)));
		tmp = max(tmp, dp[status | (1 <<(2*i))]);
		
		dfs(status | (2 <<(2*i)));
		tmp = max(tmp, dp[status | (2 <<(2*i))]);
		if(tmp >= 0)
	    	dp[status] = min(dp[status], tmp+1);
	}	
	//show(status);
	//printf(": %d\n", dp[status]);
	return;
}

void solve() {
	scanf("%d%d%d", &R, &C, &W);
	memset(dp, -1, sizeof(dp));
	dfs(0);
	printf("%d\n", dp[0]);
	//exit(0);
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}