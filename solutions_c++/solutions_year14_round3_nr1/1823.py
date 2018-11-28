#include <stdio.h>


int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-out.txt", "w", stdout);

	long long arr[40] = { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768 };

	int tc, i, p, q, j, c;
	bool flag;

	for (i = 15; i < 40; i++)
		arr[i] = arr[i - 1] * 2;

	scanf("%d", &tc);

	for (i = 1; i <= tc; i++) {

		scanf("%d/%d", &p, &q);
		c = 0;
		flag = false;

		for (j = 0; j < 40; j++) {

			if (arr[j] % q == 0) {

				while (1) {
					p *= 2;
					c++;

					if (p >= q) {
						printf("Case #%d: %d\n", i, c);
						break;
					}

					if (c > 40) {
						printf("Case #%d: impossible\n", i);
						break;
					}
				}

				flag = true;
				break;
			}
		}

		if (flag == false)
			printf("Case #%d: impossible\n", i);
	}
	return 0;
}