#include<bits/stdc++.h>
using namespace std;
const int N = 105;
char s[N];
int a[N];
int main() {
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		printf("Case #%d: ", tt);
		scanf("%s", s);
		int l = strlen(s);
		int ans = 0;
		for (int i = l - 1; i >= 0; --i) {
			if (s[i] == '-') {
				if (s[0] == '+') {
					int t = 0;
					++ans;
					while (s[t] == '+')	s[t] = '-', ++t;
				}
				++ans;
				reverse(s, s + i + 1);
				for (int j = 0; j <= i; ++j) {
					if (s[j] == '+')	s[j] = '-';
					else s[j] = '+';
				}
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
