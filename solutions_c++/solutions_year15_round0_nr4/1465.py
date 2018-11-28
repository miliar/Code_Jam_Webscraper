#include <cstdio>

bool check(int X, int R, int C)
{
	if (X == 1) return 1;
	if (X == 2) return (R == 2 || C == 2 || R == 4 || C == 4);
	if (X == 3) return !(R == 1 || C == 1 || (C == 2 && R == 2) || (R == 2 && C == 4) || (R == 4 && C == 2) || (R == 4 && C == 4));
	if (X == 4) return ((R == 3 && C == 4) || (R == 4 && C == 3) || (R == 4 && C == 4));
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		int X, R, C;
		scanf("%d%d%d", &X, &R, &C);
		if (check(X, R, C))
			printf("Case #%d: GABRIEL\n", cases);
		else
			printf("Case #%d: RICHARD\n", cases);
	}
}

