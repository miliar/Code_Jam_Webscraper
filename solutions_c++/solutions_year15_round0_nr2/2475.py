#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

int cnt[1010];
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int cas;
	cin >> cas;
	for (int t = 1; t <= cas; t++) {
		memset(cnt, 0, sizeof(cnt));
		int n;
		cin >> n;
		for (int i = 1; i <= n; i++) {
			int tmp;
			cin >> tmp;
			cnt[tmp]++;
		}
		int ans = 1000;
		for (int tt = 1; tt <= 1000; tt++) {
			int tmp = tt;
			for (int i = 1; i <= 1000; i++) {
				tmp += (i - 1) / tt * cnt[i];
			}
			ans = min(ans, tmp);
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}