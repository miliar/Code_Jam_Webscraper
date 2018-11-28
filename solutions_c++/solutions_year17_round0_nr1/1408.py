#include <stdio.h>
#include <iostream>
#include <string>
#include <assert.h>

using namespace std;
typedef long long ll;

int solve(void) {
	string s; cin >> s;
	int K; scanf("%d", &K);
	int ans = 0;
	for (int i=0; i<s.length(); i++) {
		if (s[i] == '+') continue;
		else if (s[i] == '-') {
			if (i+K <= s.length()) {
				ans++;
				for (int j=i; j<i+K; j++) {
					s[j] = (s[j]=='+'?'-':'+');
				}
			}
			else {
				return -1;
			}
		}
		else {
			assert(0);
		}

	}
	return ans;
}
int main(void) {
	int T; scanf("%d", &T);
	for (int tc=1; tc<=T; tc++) {
		printf("Case #%d: ", tc);
		int ret = solve();
		if (ret >= 0) {
			printf("%d\n", ret);
		}
		else {
			printf("%s\n", "IMPOSSIBLE");
		}
	}
}
