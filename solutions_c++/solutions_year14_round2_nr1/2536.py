#include <iostream>
#include <cstdio>

using namespace std;

int T, n;
int num[105][105], cnt;
string inp, temp, all;
bool ans;

int main()
{
freopen("A-small.in", "r", stdin);
freopen("A-small.out", "w", stdout);
  cin >> T;
	for (int Case = 1; Case <= T; ++Case) {
		cin >> n;
		ans = true;
		all = "";
		for (int i = 0; i < n; ++i) {
			cin >> inp;
			cnt = 0;
			temp = "";
			temp += inp[0];
			num[i][cnt] = 1;
			for (int j = 1; inp[j] != '\0'; ++j) {
				if (inp[j] != inp[j - 1]) {
					temp += inp[j];
					num[i][++cnt] = 1;
				} else {
					num[i][cnt]++;
				}
			}
			if (all == "")
				all = temp;
			else if (all != temp)
				ans = false;
		}
		printf("Case #%d: ", Case);
		if (!ans) {
			printf("Fegla Won\n");
			continue;
		}
		int ans = 0;
		for (int i = 0; i <= cnt; ++i) {
			int tot = 0;
			for (int j = 0; j < n; ++j)
				tot += num[j][i];
			tot /= n;
			for (int j = 0; j < n; ++j)
				ans += (tot - num[j][i] > 0) ? (tot - num[j][i]) : (num[j][i] - tot);
		}
		printf("%d\n", ans);
	}
	return 0;
}
