#include <stdio.h>

int t, cas;
int x, r, c;

bool solve() {
	if (x == 1)				//.
		return true;
	else if (x == 2) {		//..
		if ((r * c) % 2 == 0)
			return true;
		else
			return false;
	} else if (x == 3) {	//...  L
		if (r >= 2 && c >= 2 && (r * c) % 3 == 0)
			return true;
		else
			return false;
	} else if (x == 4) {
		if (r * c == 12 || r * c == 16)
			return true;
		else
			return false;
	} else {
		return false;
	}
	
}

int main() {
	scanf("%d", &t);
	for (cas = 1; cas <= t; cas++) {
		scanf("%d%d%d", &x, &r, &c);
		bool ret = solve();
		printf("Case #%d: %s\n", cas, ret ? "GABRIEL" : "RICHARD");
	}
	return 0;
}