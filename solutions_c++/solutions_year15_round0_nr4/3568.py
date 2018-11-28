#include <stdio.h>
#include <stdlib.h>

int main()
{

	freopen("D-small-attempt1.in", "r", stdin);
	freopen("Dsmall1.out", "w", stdout);

	int precomputed[10][3] = {	{0, 0, 0}, // 1
								{1, 0, 0}, // 2
								{0, 0, 0}, // 3
								{1, 0, 0}, // 4
								{1, 0, 0}, // 4
								{1, 1, 0}, // 6
								{1, 0, 0}, // 2*4
								{0, 1, 0}, // 3*3
								{1, 1, 1}, // 3*4
								{1, 0, 1}

	};

	int tc, i, k, c, r, ans;

	scanf("%d", &tc);

	for (i = 1; i <= tc; i++) {

		scanf("%d%d%d", &k, &r, &c);

		//printf("\n%d %d %d\n", k, r, c);
		if (k == 1) {
			printf("Case #%d: GABRIEL\n", i);
			continue;
		}

		switch (r*c) {

		case 1:
		case 2:
		case 3:
			ans = precomputed[r*c - 1][k - 2];
			break;
		
		case 4:
			if (r == 1 || c == 1)
				ans = precomputed[r*c - 1][k - 2];
			else
				ans = precomputed[4][k - 2];
			break;

		case 6:
			ans = precomputed[5][k - 2];
			break;

		case 8:
			ans = precomputed[6][k - 2];
			break;

		case 9:
			ans = precomputed[7][k - 2];
			break;

		case 12:
			ans = precomputed[8][k - 2];
			break;

		case 16:
			ans = precomputed[9][k - 2];
			break;

		default:
			printf("ERROR ERROR\n");
			break;
		}

		if (ans == 0)
			printf("Case #%d: RICHARD\n", i);
		else
			printf("Case #%d: GABRIEL\n", i);
	}
	
	return 0;
}