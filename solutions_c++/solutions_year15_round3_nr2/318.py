#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

class Solution1 {
public:
	void solve() {
		int tcase, r, c, w;
		cin >> tcase;
		for (int tcase_idx = 1; tcase_idx <= tcase; tcase_idx++) {
			cin >> r >> c >> w;
			int a = c / w;
			int b = c % w;
			int ans = a * r + (b == 0 ? w - 1 : w);

			printf("Case #%d: %d\n", tcase_idx, ans);
		}
	}
};

class Solution2 {
public:
	void solve() {
		int tcase, k, l, s;
		string k_str, l_str;
		double frequency[26];
		cin >> tcase;
		for (int tcase_idx = 1; tcase_idx <= tcase; tcase_idx++) {
			cin >> k >> l >> s;
			cin >> k_str >> l_str;
			memset(frequency, 0, sizeof(frequency));
			for (int i = 0; i < k; i++) {
				frequency[k_str[i]-'A'] += 1.0 / k;
			}
			if (!check_frequency(frequency, l_str)) {
				printf("Case #%d: 0.0\n", tcase_idx);
				continue;
			}
			int total_bring = get_total_bring(l_str, s);
//			cout << "@" << total_bring << endl;
			double pay = 1;
			for (int i = 0; i < l; i++) {
				pay = pay * frequency[l_str[i]-'A'];
			}
			pay *= (s-l+1);
			printf("Case #%d: %.7lf\n", tcase_idx, total_bring - pay);
		}
	}
	bool check_frequency(double *frequency, string &l_str) {
		for (int i = 0; i < l_str.size(); i++) {
			if (frequency[l_str[i]-'A'] <= 0.0) return false;
		}
		return true;
	}
	int get_total_bring(string &l_str, int s) {
		int l = l_str.size();
		if (s == l) return 1;
		int len;
		for (len = 1; len <= l; len++) {
			bool check = true;
			for (int i = 0; i < l-len; i++) {
//				printf("len:%d, i:%d, i+len:%d\n", len, i, i+len);
				if (l_str[i] != l_str[i+len]) {
					check = false;
					break;
				}
			}
			if (check) break;
		}
		int ans = 0;
//		if (len == 0) return 1 + (s - l);
		ans = (s - l)  / len;
		ans += 1;
		return ans;
	}
};

int main() {
	Solution2 solution;
	solution.solve();
	return 0;
}
