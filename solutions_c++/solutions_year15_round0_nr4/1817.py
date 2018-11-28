#include <stdio.h>

using namespace std;

int main()
{
	freopen("inputOminousOmino.in", "r", stdin);
	freopen("outputOminousOmino.out", "w", stdout);

	int T, R, X, C, aux;

	scanf("%d", &T);

	for (int count = 1; count <= T; ++count) {
		printf("Case #%d: ", count);

		scanf("%d %d %d", &X, &R, &C);
		if (R > C) {
			aux = R;
			R = C;
			C = aux;
		}

		if (X == 1) {
			printf("GABRIEL\n");
			continue;
		}

		if (X == 2) {
			if (R == 1) {

				if (C == 1) printf("RICHARD\n");

				if (C == 2) printf("GABRIEL\n");

				if (C == 3) printf("RICHARD\n");

				if (C == 4) printf("GABRIEL\n");

			}

			if (R == 2) {

				if (C == 2) printf("GABRIEL\n");

				if (C == 3) printf("GABRIEL\n");

				if (C == 4) printf("GABRIEL\n");

			}

			if (R == 3) {

				if (C == 3) printf("RICHARD\n");

				if (C == 4) printf("GABRIEL\n");

			}

			if (R == 4) printf("GABRIEL\n");

		}

		if (X == 3) {
			if (R == 1) {

				if (C == 1) printf("RICHARD\n");

				if (C == 2) printf("RICHARD\n");

				if (C == 3) printf("RICHARD\n");

				if (C == 4) printf("RICHARD\n");

			}

			if (R == 2) {

				if (C == 2) printf("RICHARD\n");

				if (C == 3) printf("GABRIEL\n");

				if (C == 4) printf("RICHARD\n");

			}

			if (R == 3) {

				if (C == 3) printf("GABRIEL\n");

				if (C == 4) printf("GABRIEL\n");

			}


			if (R == 4) printf("RICHARD\n");

		}

		if (X == 4) {
			if (R == 1) {

				if (C == 1) printf("RICHARD\n");

				if (C == 2) printf("RICHARD\n");

				if (C == 3) printf("RICHARD\n");

				if (C == 4) printf("RICHARD\n");

			}

			if (R == 2) {

				if (C == 2) printf("RICHARD\n");

				if (C == 3) printf("RICHARD\n");

				if (C == 4) printf("RICHARD\n");

			}

			if (R == 3) {

				if (C == 3) printf("RICHARD\n");

				if (C == 4) printf("GABRIEL\n");

			}


			if (R == 4) printf("GABRIEL\n");

		}

		
	}

	return 0;
}