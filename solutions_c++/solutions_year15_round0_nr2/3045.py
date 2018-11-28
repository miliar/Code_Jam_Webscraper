#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

int num[1010], n;

void input() {
	scanf("%d", &n);
	for(int i = 0;i < n;i ++) scanf("%d", &num[i]);
}

void solve() {
	sort(num, num+n);
	//printf("%d\n", num[n-1]);
	int res = num[n-1];
	for(int i = 1;i < res;i ++) {
		int tt = 0;
		for(int j = 0;j < n;j ++) tt += (num[j] + i-1)/i - 1;
		if(tt + i < res) res = tt + i;
	}
	printf("%d\n", res);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Case;
	scanf("%d", &Case);
	for(int cas = 1;cas <= Case;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
}