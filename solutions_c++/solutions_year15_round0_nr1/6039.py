#include <bits/stdc++.h>
using namespace std;

/*
 * You got a dream, you gotta protect it.
 */

typedef long long ll;

char s[1111];

int main(int argc, char **argv) {
//	freopen("A-large.in", "r", stdin);
//	freopen("output.txt", "w", stdout);
	int t, k = 1;
	scanf("%d", &t);
	while (t--) {
		int n;
		scanf("%d%s", &n, s);
		int with = s[0] - '0', res = 0;
		for (int i = 1; i <= n; ++i) {
			if (with < i && s[i] != '0') {
				res += i - with;
				with = i;
			}
			with += s[i] - '0';
		}
		printf("Case #%d: %d\n", k++, res);
	}
	return 0;
}
