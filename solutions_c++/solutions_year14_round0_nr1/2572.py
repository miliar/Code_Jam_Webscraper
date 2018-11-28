#include <stdio.h>
#include <stdlib.h>

using namespace std;

int m1[10][10], m2[10][10], r1, r2;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T = 0;
	scanf("%d", &T);
	for (int q = 0; q < T; q++)
	{
		scanf("%d", &r1);
		r1 --;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d", &m1[i][j]);

		scanf("%d", &r2);
		r2 --;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d", &m2[i][j]);

		int count = 0, place = -1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (m2[r2][i] == m1[r1][j])
				{
					count++;
					place = i;
				}

		printf("Case #%d: ", q + 1);
		if (count == 0)
		{
			printf("%s", "Volunteer cheated!");
		} else
		if (count > 1)
		{
			printf("%s", "Bad magician!");
		} else
		if (count == 1)
		{
			printf("%d", m2[r2][place]);
		}
		if ( q != T - 1 )
			printf("\n");
	}
	return 0;
}