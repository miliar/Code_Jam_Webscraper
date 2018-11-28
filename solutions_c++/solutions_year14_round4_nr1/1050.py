#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <set>
#include <algorithm>
#include <queue>

#pragma warning(disable: 4996)

using namespace std;

int num[10000], X, n;

void input() {
	scanf("%d%d", &n, &X);
	for(int i = 0;i < n;i ++) scanf("%d", &num[i]);
}

void solve() {
	sort(num, num+n);

	int res = 0, b = 0;
	for(int i = n-1;i >= b;i --) {
		if(num[i] + num[b] <= X) ++ b;
		++ res;
	}

	printf(" %d\n", res);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int cas = 1;cas <= t;cas ++) {
		input();
		printf("Case #%d:", cas);
		solve();
	}
	return 0;
}