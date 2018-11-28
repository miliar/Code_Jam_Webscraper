#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <climits>
#include <complex>
#include <fstream>
#include <cassert>
#include <cstdio>
#include <bitset>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <ctime>
#include <set>
#include <map>
#include <cmath>

using namespace std;

const int maxn = 111;
char pan[maxn];
bool vis[maxn];
int ans, n;
char st[maxn];
int top;
int dp[maxn][maxn];

bool check() {
	for(int i = 0; i < n; i++)
		if(pan[i] == '-') return 0;
	return 1;
}

void flip(int rr) {
	top = 0;
	for(int i = 0; i <= rr; i++) {
		st[top++] = pan[i];
	}
	for(int i = 0; i <= rr; i++) {
		if(st[--top] == '+') pan[i] = '-';
		else pan[i] = '+';
	}
}

void dfs(int pos, int cnt) {
	if(cnt >= ans) return;
	if(check()) {
		if(cnt < ans) ans = cnt;
		return;
	}
	for(int i = 0; i < n; i++) {
		if(!vis[i]) {
			vis[i] = 1;
			flip(i);
			dfs(i, cnt+1);
			flip(i);
			vis[i] = 0;
		}
	}
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int _ = 1; _ <= T; _++) {
		printf("Case #%d: ", _);
		memset(vis, 0, sizeof(vis));
		memset(dp, -1, sizeof(dp));
		ans = 0x7f7f7f;
		scanf("%s", pan);
		n = strlen(pan);
		dfs(0, 0);
		printf("%d\n", ans);
	}
	return 0;
}