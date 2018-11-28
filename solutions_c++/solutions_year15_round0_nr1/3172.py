#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

int num[1024], n;

void input() {
	scanf("%d", &n);
	char buf[1024];
	scanf("%s", buf);
	for(int i = 0;i <= n;i ++) num[i] = buf[i]-'0';
}

void solve() {
	int res = 0, current = num[0];
	for(int i = 1;i <= n;i ++) for(int j = 0;j < num[i];j ++) {
		if(current < i) {
			res += (i-current);
			current = i;
		}
		++ current;
	}
	printf("%d\n", res);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Case;
	scanf("%d", &Case);
	for(int cas = 1;cas <= Case;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
}