#include <bits/stdc++.h>
using namespace std;

int main(void) {
	int t, n;
	char s[1004]; freopen("in.txt", "r", stdin); freopen("out.out", "w", stdout);
	cin >> t;

	for (int te = 1; te <= t; te++) {
		cin >> n >> s;

		
		int cont = 0, ans = 0, m = 0;

		for (int i = n; i >= 0; --i) {
			if ((s[i] - '0') > 0) {
				m = i;
				break;
			}
		}

		for (int i = 0; i <= n; i++) {
			if (cont < i)
				ans++, cont++;
			cont += s[i] - '0';
		}

		printf("Case #%d: %d\n", te, ans);
	}

	return 0;
}