#include <stdio.h>
int main() {
	int TC;
	scanf("%d", &TC);
	for(int tc = 1; tc <= TC; tc++) {
		int x, r, c;
		bool tr = false;
		scanf("%d%d%d", &x, &r, &c);
		if (x == 1) tr = true;
		else if (x == 2) {
			if (((r * c) % 2) == 0) tr = true;
		} else if (x == 3) {
			if ((((r * c) % 3) == 0) && (r != 1) && (c != 1)) tr = true;
		} else {
			if ((r == 4 && c == 4) || (r == 4 && c == 3) || (r == 3 && c == 4)) tr = true;	
		}

		if (!tr) printf("Case #%d: RICHARD\n", tc);
		else printf("Case #%d: GABRIEL\n", tc);
	}
}