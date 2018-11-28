#include "template.h"

int main() {
	cin.sync_with_stdio(false);

	freopen("B-large.in", "r", stdin);
	freopen("output_B.txt", "w", stdout);

	int TC; cin >> TC;
	for (int tc = 1; tc <= TC; ++tc) {
		string s;
		cin >> s;
		int ans = -1;

		//중복원소제거
		auto it = unique(s.begin(), s.end());
		s.erase(it, s.end());

		int len = s.size();
		char backChar = s.back();

		if (backChar == '-') {
			ans = len;
		}
		else {
			ans = len - 1;
		}

		printf("Case #%d: %d\n", tc, ans);
	}
}