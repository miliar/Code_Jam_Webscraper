#include <bits/stdc++.h>
using namespace std;



int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int k = 1;k <= t;k++) {
		int n;
		string s;
		cin >> n >> s;
		int ans = 0, sum = 0;
		for(int i = 0;i < (int)s.size();i++) {
			if(i > sum) {
				ans += i - sum;
				sum += i - sum;
			}
			sum += s[i] - '0';
		}
		cout << "Case #" << k << ": " << ans << endl;
	}
	return 0;
}















//long long arr[100005], sum[100005], ans, n;
//
//int main() {
//	cin >> n;
//	long long mx = 0;
//	for(int i = 0;i < n;i++) {
//		cin >> arr[i];
//		mx = max(mx, arr[i]);
//		sum[i] = mx - arr[i];
//	}
//	mx = 0;
//	for(int i = 0;i < n;i++) {
//		if(sum[i] >= mx or i == n - 1) {
//			ans += mx;
//			mx = sum[i];
//		}
//	}
//	cout << ans;
//	return 0;
//}
