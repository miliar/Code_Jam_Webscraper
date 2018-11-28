#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

bool vis[10];
int ans, n;

void solve (long long num) {
	while (num) {
		int x = num%10;
		if (!vis[x]) {
			ans += x;
			vis[x] = 1;
		}
		num /= 10;
	}
}

int main () {
	freopen ("in", "r", stdin);
	freopen ("out", "w", stdout);
	int t, kase = 0;
	scanf ("%d", &t);
	while (t--) {
		//for (n = 0; n <= 1000000; n++) {
		ans = 0;
		memset (vis, 0, sizeof vis);
		scanf ("%d", &n);
		printf ("Case #%d: ", ++kase);
		if (n == 0) {
			printf ("INSOMNIA\n");
			continue;
		}
		for (int i = 1; ; i++) {
			solve (1LL*i*n);
			if (ans == 45 && vis[0]) {
				printf ("%d\n", i*n);
				break;
			}
		}
		//}
	}
	return 0;
}