#include <bits/stdc++.h>
using namespace std;

int getint() {
	char c = ' ';
	for(; c < '0' || c > '9'; c = getchar());
	int ret = 0;
	for(; c >= '0' && c <= '9'; c = getchar()) ret = ret * 10 + c - '0';
	return ret;
}

const int N = 1010;
char data[N];
int n, k, w[N];

void solve() {
	n = strlen(data);
	for(int i = 0; i < n; ++i) w[i] = data[i] == '-';
	int ans = 0;
	for(int i = 0; i + k <= n; ++i) {
		if(!w[i]) continue;
		++ans;
		for(int j = i; j < i + k; ++j) w[j] ^= 1;
	}
	for(int i = 0; i < n; ++i)
		if(w[i]) {
			ans = -1;
			break;
		}
	if(ans < 0) puts("IMPOSSIBLE");
	else printf("%d\n", ans);
}

int main() {
	for(int cases = getint(), idx = 1; idx <= cases; ++idx) {
		printf("Case #%d: ", idx);
		scanf("%s%d", data, &k);
		solve();
	}
	return 0;
}

