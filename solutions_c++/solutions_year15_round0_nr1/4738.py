#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main() {

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int tests, t = 0;
	scanf("%d", &tests);
	while (tests--) {

		int smax; string s;
		cin >> smax;
		cin >> s;

		int in = 0, sol = 0;
		for (int i = 0; i < s.size(); ++i) {

			int needed = max(0, i - in);
			sol += needed;
			in += s[i] - '0' + needed;
		}

		printf("Case #%d: %d\n", ++t, sol);
	}

	return 0;
}