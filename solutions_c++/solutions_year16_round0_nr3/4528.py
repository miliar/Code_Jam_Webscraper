#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
LL n;
int main() {
	cin >> n;
	LL arr[n], cnt[n], temp = 0, ans = 0, sum = 0;
	memset(cnt, 0, sizeof cnt);
	for (int i = 0; i < n; i++)
		cin >> arr[i], sum += arr[i];
	if (sum % 3 != 0) {
		printf("0\n");
		return 0;
	}
	for (int i = n - 1; i >= 0; i--) {
		temp += arr[i];
		if (temp == sum / 3)
			cnt[i] = 1;
	}
	for (int i = n - 2; i >= 0; i--)
		cnt[i] += cnt[i + 1];
	temp = 0;
	for (int i = 0; i < n - 2; i++) {
		temp += arr[i];
		if (temp == sum / 3)
			ans += cnt[i + 2];
	}
	cout << ans << endl;
	return 0;
}
