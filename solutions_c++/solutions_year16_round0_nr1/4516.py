#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int T;
long long n;
int cnt, ans;
bool vis[12];

void count(long long x) {
	while (x) {
		int tmp = x % 10;
		if (!vis[tmp]) {
			vis[tmp] = 1;
			cnt++;
		}
		x /= 10;
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ca++) {
		scanf("%lld", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", ca);
		} else {
			cnt = 0;
			memset(vis, 0, sizeof(vis));
			ans = 0;
			while (cnt < 10) {
				ans++;
				count(n * ans);
			}
			printf("Case #%d: %lld\n", ca, ans * n);
		}
	}
}