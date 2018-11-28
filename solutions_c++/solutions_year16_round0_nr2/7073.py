#include <bits/stdc++.h>

using namespace std;

int main() {
	int i, j, tt, l;
	int ans;
	char s[105];
	scanf("%d ", &tt);
	for (int cc = 1; cc <= tt; cc++) {
		ans = 0;
		fgets(s, 105, stdin);
		l = strlen(s);
		for (i = l - 1; i >= 0; i--) {
			if (s[i] == '-') {
				for (j = i; j >= 0; j--)
					s[j] = s[j] == '+' ? '-' : '+';
				++ans;
			}
		}
		printf("Case #%d: %d\n", cc, ans);
	}
	return 0;
}
