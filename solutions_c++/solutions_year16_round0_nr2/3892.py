#include<bits/stdc++.h>
using namespace std;

inline void flip(string &s, short j) {
	for (short i = 0; i <= j; ++i)
		s[i] = (s[i] == '+' ? '-' : '+');
	reverse(s.begin(), s.begin() + j + 1);
}


inline short solve(string &s) {
	short ans = 0;
	for (short i = s.size() - 1; i >= 0; --i)
		if (s[i] == '-') {
			if (s[0] == '+') {
				++ans;
				flip(s, s.find('-') - 1);
			}
			++ans;
			flip(s, i);
		}
	return ans;
}

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	string s;
	cin >> t;
	for (int cs = 1; cs <= t; ++cs) {
		cin >> s;
		cout << "Case #" << cs << ": " << solve(s) << '\n';
	}

	return 0;
}
