#include <stdio.h>
bool f(int x, int r, int c) {
	if (x == 1)
		return true;
	if (x == 2)
		return !(r % 2 == 1 && c % 2 == 1);
	if (x == 3)
		return (r == 2 && c == 3) || (r == 3 && c == 2) || (r == 3 && c == 3)
				|| (r == 3 && c == 4) || (r == 4 && c == 3);
	if (x == 4)
		return (r == 3 && c == 4) || (r == 4 && c == 3) || (r == 4 && c == 4);
	return false;
}
int main() {
	int t, cas = 0;
	int n, i, j, k;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d%d%d", &i, &j, &k);
		if (f(i, j, k))
			printf("Case #%d: GABRIEL\n", cas);
		else
			printf("Case #%d: RICHARD\n", cas);

	}
}

