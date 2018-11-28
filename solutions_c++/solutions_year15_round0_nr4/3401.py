#include<stdio.h>
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t,cccc=0;
	for (scanf("%d", &t); t--;) {
		cccc++;
		int x, r, c;
		scanf("%d %d %d", &x, &r, &c);
		if (x == 1)
			printf("Case #%d: GABRIEL\n",cccc);
		else if (x == 2 && (r*c) % 2 == 0) 
			printf("Case #%d: GABRIEL\n", cccc);
		else if (x == 3 && (r*c) % 3 == 0 && r > 1 && c > 1) 
			printf("Case #%d: GABRIEL\n", cccc);
		else if (x == 4 && ((r == 4 && c == 4) || (r == 4 && c == 3) || (r == 3 && c == 4)))
			printf("Case #%d: GABRIEL\n", cccc);
		else
			printf("Case #%d: RICHARD\n", cccc);
	}
	return 0;
}