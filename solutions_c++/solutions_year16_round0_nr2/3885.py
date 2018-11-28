#include <bits/stdc++.h>

using namespace std;

long long solve() {
	string s;
	cin >> s;
	long long ans = 0;
	while (count(s.begin(), s.end(), '+') != (int)s.size()) {
		if (s[0] == '+') {
			int pos = 0;
			while (s[pos] != '-') {
				s[pos] = '-';
				++pos;	
			}
			ans++;
		} else {
			int last = (int)s.size() - 1;
			while (s[last] == '+') {
				--last;
			}
			for (int i = 0; i <= last; ++i) {
				if (s[i] == '-') {
					s[i] = '+';
				} else {
					s[i] = '-';
				}
			}
			reverse(s.begin(), s.begin() + last + 1);
			++ans;
		}
	}
	return ans;
}

int main() {
#ifdef ALEXEY
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
#endif
	int test_count;
	cin >> test_count;
	for (int i = 1; i <= test_count; ++i) {
		cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}
