#include <stdio.h>

using namespace std;

int main()
{
	freopen("inputDijkstra.in", "r", stdin);
	freopen("outputDijkstra.out", "w", stdout);

	int T, L, X;
	char string[10010];
	int vect[10010];

	int currentValue = 1;
	long long currentPos = 0;
	long long il;

	int M[5][5] = {0, 0, 0, 0, 0,
		0, 1,  2,  3,  4,
		0, 2, -1,  4, -3,
		0, 3, -4, -1,  2,
		0, 4,  3, -2, -1 };

	int value;

	scanf("%d", &T);

	for (int count = 1; count <= T; ++count) {
		printf("Case #%d: ", count);

		scanf("%d %d", &L, &X);

		scanf("%s", string);
		for (int i = 0; i < L; ++i) {
			if (string[i] == 'i')
				vect[i] = 2;
			if (string[i] == 'j')
				vect[i] = 3;
			if (string[i] == 'k')
				vect[i] = 4;
		}

        value = 2;
		currentPos = 0;
		currentValue = 1;
		il = 0;

		while (currentPos < L * X) {

			il = currentPos;

			while (il >= L)
				il -= L;

			if (currentValue > 0)
				currentValue = M[currentValue][vect[il]];
			else
				currentValue = -M[-currentValue][vect[il]];

			if (currentValue == value && value != 4)
				++value, currentValue = 1;

			++currentPos;
		}

		if (value == 4 && currentValue == 4)
			printf("YES\n");
		else printf("NO\n");

	}

	return 0;
}
