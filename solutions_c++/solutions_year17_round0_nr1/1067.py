#include <bits/stdc++.h>

using namespace std;

int main()
{
	int ntc;
	scanf("%d", &ntc);
	for (int itc = 1; itc <= ntc; ++itc) {
		int k;
		string s;
		cin >> s >> k;
		printf("Case #%d: ", itc);
		int ans = 0;
		bool ok = true;
		for (int i = 0; i < s.size(); ++i) {
			if (s[i] == '-') {
				if (i+k <= s.size()) {
					++ans;
					for (int j = i; j < i+k; ++j) {
						s[j] = (s[j] == '+') ? '-' : '+';
					}
				}
				else {
					ok = false;
					break;
				}
			}
		}
		if (ok) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
}
