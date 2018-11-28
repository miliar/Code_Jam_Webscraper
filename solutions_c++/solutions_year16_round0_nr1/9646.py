#include <bits/stdc++.h>
using namespace std;
bool ok[10];
bool check(int x) {
	while (x) {
		ok[x % 10] = 1;
		x /= 10;
	}
	bool f = 1;
	for (int i = 0; i < 10; ++i)
		if (!ok[i])	f = 0;
	return f;
}
int main() {
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		memset(ok, 0, sizeof(ok));
		printf("Case #%d: ", tt);
		int x;
		scanf("%d", &x);
		if (!x)	puts("INSOMNIA");
		else {
			int ans;
			for (int i = 1; i <= 100; ++i)
				if (check(x * i)) {
					ans = x * i;
					break;
				}
			printf("%d\n", ans);
		}
	}
	return 0;
}
