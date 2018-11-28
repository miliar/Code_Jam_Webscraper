#include<cstdio>

int find_ans(int x, int r, int c) {
	if (x == 1) return 1;
	if ((r*c)%x != 0) return 0;
	if (x == 2) return 1;
	if (x == 3) {
		if (r*c == 3) return 0;
		else  return 1;
	}
	if (x == 4) {
		if (r*c <= 8) return 0;
		else return 1;
	}
}
int main() {
	int T;
	scanf("%d", &T);
	for (int nm=1;nm<=T;nm++) {
		int x, r, c;
		scanf("%d%d%d", &x, &r, &c);
		int ans = find_ans(x, r, c);
		if (ans) {
			printf("Case #%d: GABRIEL\n", nm);
		}
		else {
			printf("Case #%d: RICHARD\n", nm);
		}
	}
	return 0;
}
