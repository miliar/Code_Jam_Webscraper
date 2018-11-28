#include <bits/stdc++.h>
using namespace std;

int n; char s[10010];
int main() {
	int T; scanf("%d", &T); for(int ks = 1; ks <= T; ++ks) {
		scanf("%d%s", &n, s);
		int cur = 0, ans = 0;
		for(int i = 0; i <= n; ++i) {
			int t = s[i] - '0';
			if(i <= cur) {
				cur += t;
			}
			else {
				ans += i - cur;
				cur += i - cur;
				cur += t;
			}
		}
		printf("Case #%d: %d\n", ks, ans);
	}
	return 0;
}
