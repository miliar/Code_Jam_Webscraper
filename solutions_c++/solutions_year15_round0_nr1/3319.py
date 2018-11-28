#include <bits/stdc++.h>
using namespace std;

int main() {
	int T; scanf ("%d", &T);
	for (int i = 0; i < T; i++) {
		printf ("Case #%d: ", i + 1);
		int n;
		char str[1005];
		scanf ("%d %s", &n, str);
		int cnt = 0, ans = 0;
		for (int j = 0; j <= n; j++) {
			if (str[j] == '0')  continue;
			if (cnt < j) {
				ans += j - cnt;
				cnt = j;
			}
			cnt += str[j] - '0';
		}
		printf ("%d\n", ans);
	}
	return 0;
}
