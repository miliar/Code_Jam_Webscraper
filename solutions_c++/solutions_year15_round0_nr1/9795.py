#include <stdio.h>
#include <stdlib.h>

int main()
{

	freopen("A-small-attempt1.in", "r", stdin);
	freopen("Asmall1.out", "w", stdout);

	int tc, s, i, j, curr, stood, fr;
	char sm[1001];

	scanf("%d", &tc);

	for (i = 1; i <= tc; i++) {

		scanf("%d", &s);
		scanf("%s", sm);

		//printf("%d\t%s\n", s, sm);
		curr = stood = fr = 0;

		for (j = 0; j <= s; j++) {

			curr = sm[j] - 48;

			if (curr == 0)
				continue;

			if (j <= stood) {
				stood += curr;
			}
			else {

				fr += (j - stood);
				stood += (fr + curr);
			}
		}

		printf("Case #%d: %d\n", i, fr);
	}

	return 0;
}