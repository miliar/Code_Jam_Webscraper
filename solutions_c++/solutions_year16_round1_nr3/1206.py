#include <algorithm>
#include <assert.h>
#include <iostream>
#include <string.h>
#include <memory.h>
#include <stdio.h>
#include <vector>
#include <time.h>
#include <string>
#include<bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <deque>
#include <map>
using namespace std;
typedef long long ll;
const int N = 10+ 10;
int n,bff[N],ans;
bool vis[N];
int root;
void dfs(int u,int d,int p) {
	vis[u] = true;
	if (u == root)
		ans = max(ans, d);
	if (!vis[bff[u]])
		dfs(bff[u],d+1,u);
	else if (bff[u] == p) {
		ans = max(ans, d);
		for (int i = 0; i < n; ++i)
			if (!vis[i])
				dfs(i, d + 1, u);
	}
	else if(bff[u]==root)
		ans = max(ans, d);
	vis[u] = false;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
#endif
	int t,cas=1;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", bff + i),bff[i]--;
		ans = 0;
		for (int i = 0; i < n; ++i) {
			root = i;
			dfs(i, 0, -1);
		}
		printf("Case #%d: %d\n", cas++, ans+1);
	}

	

	return 0;
}