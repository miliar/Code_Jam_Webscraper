#include <cstdio>

int main() {
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("D-small-attempt2.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++cas) {
		int x, r, c;
		scanf("%d%d%d", &x, &r, &c);
		bool canWin = true;
		if (x == 2) {
			if (r % 2 != 0 && c % 2 != 0) canWin = false;
		}
		else if (x == 3) {
			canWin = false;
			if (r >= 2 && c == 3) canWin = true;
			if (r == 3 && c >= 2) canWin = true;
		}
		else if (x == 4) {
			canWin = false;
			if (r == 3 && c == 4) canWin = true;
			if (r == 4 && c == 3) canWin = true;
			if (r == 4 && c == 4) canWin = true;
		}
		printf("Case #%d: %s\n", cas, canWin ? "GABRIEL" : "RICHARD");
	}
	return 0;
}

