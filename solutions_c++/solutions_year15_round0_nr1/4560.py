#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;

	for (int test = 1; test <= t; test++) {
		int s_max;
		cin >> s_max;

		string s;
		cin >> s;

		vector<int> a(s.length());
		for (int i = 0; i < s.length(); i++) {
			a[i] = s[i] - '0';
		}

		int cur_sum = 0;
		int ans = 0;
		for (int i = 0; i < s_max + 1; i++) {
			if (cur_sum < i) {
				ans += i - cur_sum;
				cur_sum += i - cur_sum;
			}

			cur_sum += a[i];
		}

		printf("Case #%d: %d\n", test, ans);
	}
}