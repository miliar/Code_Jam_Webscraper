#include <bits/stdc++.h>
using namespace std;

int main(int argc, char **argv) {
#ifndef ONLINE_JUDGE
	freopen("a.in", "r", stdin);
#endif
	int t;
	scanf("%d", &t);
	while (t--) {

		int n, arr[1001];
		scanf("%d", &n);
		char c;
		for (int i = 0; i <= n; ++i) {
			scanf(" %c", &c);
			arr[i] = c - '0';
		}
		int cnt = arr[0], ans = 0;
		for (int i = 1; i <= n; ++i) {
			if (i <= cnt)
				cnt += arr[i];
			else {
				ans += i - cnt;
				cnt += (i - cnt) + arr[i];
			}
		}
		static int cas = 1;
		printf("Case #%d: ", cas++);
		cout << ans << endl;
	}

	return 0;
}
