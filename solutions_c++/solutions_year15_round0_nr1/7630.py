#include <bits/stdc++.h>

using namespace std;

char s[1500];
int Case;

int main () {
	#ifdef lcl
		freopen ("q.in", "r", stdin);
		freopen ("q.out", "w", stdout);
	#endif
	int t; scanf ("%d", &t);

	while (t--) {
		int len; scanf ("\n%d %s", &len, s); len++;
		int up = 0, res = 0;;
		for (int i = 0; i < len; ++i) {
			s[i] -= '0';
			if (!s[i]) {
				continue;
			}
			if (up >= i) {
				up += s[i];
			} else {
				res += i - up;
				up += s[i] + i - up;
			}
		}
		printf ("Case #%d: %d\n", ++Case, res);
	}
	
	return 0;
}
