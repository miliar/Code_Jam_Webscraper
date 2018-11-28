#include <stdio.h>


int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("a-out.txt", "w", stdout);
	int tc, i, j, k, c, n, a1 ,a2;
	int arr[4][4], brr[4][4];

	scanf_s("%d", &tc);

	for (i = 1; i <= tc; i++) {

		c = 0;

		scanf_s("%d", &a1);

		for (j = 0; j < 4; j++) 
		for (k = 0; k < 4; k++)
			scanf_s("%d", &arr[j][k]);

		scanf_s("%d", &a2);

		for (j = 0; j < 4; j++)
		for (k = 0; k < 4; k++)
			scanf_s("%d", &brr[j][k]);

		for (j = 0; j < 4; j++) {
			for (k = 0; k < 4; k++)
			{
				if (arr[a1 - 1][j] == brr[a2 - 1][k]) {
					c++;
					n = arr[a1 - 1][j];
					break;
				}
			}
				
		}

		if (c > 1)
			printf("Case #%d: Bad magician!\n", i);
		else if (c == 0)
			printf("Case #%d: Volunteer cheated!\n", i);
		else if (c == 1)
			printf("Case #%d: %d\n", i, n);
	}
	return 0;
}