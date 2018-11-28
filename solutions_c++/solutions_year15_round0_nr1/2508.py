#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T, n;
	cin >> T;
	for (int cas = 1; cas <= T; cas++) {
		string str;
		cin >> n >> str;
		int ans = 0, cnt = 0;
		for (int i = 0; i <= n; i++) {
			int num = str[i] - '0';
			if (num == 0) continue;
			if (cnt < i) {
				int delta = i - cnt;
				ans += delta;
				cnt += delta;
			}
			cnt += num;
			//cout << i << ' ' << cnt << ' ' << num << ' ' << ans << endl;
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
