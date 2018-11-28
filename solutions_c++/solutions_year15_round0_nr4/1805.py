#include <cstdio>
int main() {
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D-small-attempt1.out", "w", stdout);
	int T, cnt = 1;
	scanf("%d", &T);
	while(T--) {
		int X, R, C;
		scanf("%d%d%d", &X, &R, &C);
		if(R*C == X && X != 1 && X != 2) printf("Case #%d: RICHARD\n", cnt++);
		else if(R*C % X != 0) printf("Case #%d: RICHARD\n", cnt++);
		else if(X == 4 && R*C == 8) printf("Case #%d: RICHARD\n", cnt++);
		else printf("Case #%d: GABRIEL\n", cnt++);
	}
	return 0;
}