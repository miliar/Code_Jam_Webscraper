#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

#define For(i, a, b) for(int i=a; i<b; ++i)
#define MP make_pair
#define INF (1<<30)

using namespace std;

typedef pair <int, int> ii;

int mat[5][5];

int main()
{
	int T;
	scanf("%d", &T);

	For(caso, 1, T+1)
	{
		int row, A = 0, B = 0;

		scanf("%d", &row);
		For(i, 0, 4)
			For(j, 0, 4)
				scanf("%d", &mat[i][j]);

		For(i, 0, 4)
			A |= (1<<mat[row-1][i]);

		scanf("%d", &row);
		For(i, 0, 4)
			For(j, 0, 4)
				scanf("%d", &mat[i][j]);

		For(i, 0, 4)
			B |= (1<<mat[row-1][i]);

		int C = A & B;

		printf("Case #%d: ", caso);
		if (C == 0)
			printf("Volunteer cheated!\n");
		else
		{
			int num = 0;
			For(i, 0, 17)
				if (C & (1<<i))
					num = i;

			if ((C ^ (1<<num)) == 0)
				printf("%d\n", num);
			else
				printf("Bad magician!\n");
		}
	}

	return 0;
}