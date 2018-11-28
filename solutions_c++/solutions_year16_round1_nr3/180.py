#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

int a[10005];
bool flag[1005];
int deepth[1005];
int n;
int dfs(int i, int d) {
	if (flag[i] == true) {
		return d - deepth[i];
	}
	flag[i] = true;
	deepth[i] = d;
	return dfs(a[i], d + 1);
}
int dfs2(int i, int fa) {
	int mx = 0;
	for (int j = 1; j <= n; ++j) {
		if (j != fa && a[j] == i) {
			int tmp = dfs2(j, i);
			if (mx < tmp)
				mx = tmp;
		}
	}
	return mx + 1;
}
int main() {
	int t, cas = 0;
	int i, j, k;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d", &n);
		for (i = 1; i <= n; ++i) {
			scanf("%d", &a[i]);
		}
		int ans = 0;
		int tmp = 0;
		for (i = 1; i <= n; ++i) {
			memset(flag, false, sizeof(flag));
			tmp = dfs(i, 0);
			if (tmp > ans)
				ans = tmp;
		}
		tmp = 0;
		for (i = 1; i <= n; ++i) {
			if (a[i] > i && a[a[i]] == i) {
				tmp += dfs2(i, a[i]);
				tmp += dfs2(a[i], i);
			}
		}
		if (tmp > ans)
			ans = tmp;
		printf("Case #%d: %d\n", cas, ans);
	}
}
