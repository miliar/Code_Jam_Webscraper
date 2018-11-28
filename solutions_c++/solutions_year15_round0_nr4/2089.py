#include <bits/stdc++.h>

const int N = 1001;

int x, r, c;

bool solve() {
		if (r > c)
			std::swap(r, c);
		switch (x) {
		case 1:
			return false;
		case 2:
			return (r * c) & 1;
		case 3:
			return !((r > 1) && !(r * c % 3));
		case 4:
			return !((r > 2) && (!(r & 3) || !(c & 3)));
		default:
			return true;
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int cnum = 1; cnum <= t; ++cnum) {
		scanf("%d %d %d", &x, &r, &c);
		printf("Case #%d: %s\n", cnum, solve()? "RICHARD": "GABRIEL");
	}
	return 0;
}

