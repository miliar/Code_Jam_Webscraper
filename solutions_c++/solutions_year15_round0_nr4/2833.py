#include <stdio.h>

int main() {
	int t;

	scanf("%d", &t);

	for(int i = 1; i <= t; i++) {
		int x, r, c;

		scanf("%d %d %d", &x, &r, &c);

		if(((r == 1&& c == 1)
			|| (r == 1&& c == 3)
			|| (r == 3&& c == 1)) && x == 1) {
				printf("Case #%d: GABRIEL\n", i);
				continue;
		}
		else if(((r == 1&& c == 2)
			|| (r == 1&& c == 4)
			|| (r == 2&& c == 2)
			|| (r == 2&& c == 4)
			|| (r == 4&& c == 1)
			|| (r == 4&& c == 2)
			|| (r == 2&& c == 1)) && (x == 1 || x == 2)) {
				printf("Case #%d: GABRIEL\n", i);
				continue;
		}
		else if(((r == 2&& c == 3)
			|| (r == 3&& c == 2)) && (x == 1 || x == 2 || x == 3)) {
				printf("Case #%d: GABRIEL\n", i);
				continue;
		}
		else if(((r == 3&& c == 4)
			|| (r == 4&& c == 3)) && (x == 1 || x == 2 || x == 3 || x == 4)) {
				printf("Case #%d: GABRIEL\n", i);
				continue;
		}
		else if(r == 4&& c == 4 && (x == 1 || x == 2 || x == 4)) {
				printf("Case #%d: GABRIEL\n", i);
				continue;
		}
		else if(r == 3&& c == 3 && (x == 1 || x == 3)) {
				printf("Case #%d: GABRIEL\n", i);
				continue;
		}

		printf("Case #%d: RICHARD\n", i);
	}

	return 0;
}