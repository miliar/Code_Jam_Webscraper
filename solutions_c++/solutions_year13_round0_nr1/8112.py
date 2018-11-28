#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int i, j, k, T, tx, ty, dot, x_di1, x_di2, y_di1, y_di2;
	string tmp;
	vector<string> input(4);
	vector<int> x_vert(4), y_vert(4), x_hor(4), y_hor(4);
	scanf("%d\n", &T);
	for (k=1; k<=T; k++)
	{
		for (i=0; i<4; i++)
		{
			getline(cin, input[i]);
			x_vert[i] = 0;
			y_vert[i] = 0;
			x_hor[i] = 0;
			y_hor[i] = 0;
			x_di1 = 0;
			y_di1 = 0;
			x_di2 = 0;
			y_di2 = 0;
			tx = ty = -1;
		}
		getline(cin, tmp);
		dot = 0;
		for (i=0; i<4; i++)
			for (j=0; j<4; j++)
			{
				if (input[i][j] == 'X')
				{
					x_vert[j]++;
					x_hor[i]++;
					if (i == j)
						x_di1++;
					if (i + j == 3)
						x_di2++;
				}
				else if (input[i][j] == 'O')
				{
					y_vert[j]++;
					y_hor[i]++;
					if (i == j)
						y_di1++;
					if (i + j == 3)
						y_di2++;
				}
				else if (input[i][j] == '.')
					dot++;
				else if (input[i][j] == 'T')
				{
					tx = j;
					ty = i;
				}
			}
		printf("Case #%d: ", k);
		if (x_vert[0] == 4 || x_vert[1] == 4 || x_vert[2] == 4 || x_vert[3] == 4)
			printf("X won\n");
		else if (x_hor[0] == 4 || x_hor[1] == 4 || x_hor[2] == 4 || x_hor[3] == 4)
			printf("X won\n");
		else if (y_vert[0] == 4 || y_vert[1] == 4 || y_vert[2] == 4 || y_vert[3] == 4)
			printf("O won\n");
		else if (y_hor[0] == 4 || y_hor[1] == 4 || y_hor[2] == 4 || y_hor[3] == 4)
			printf("O won\n");
		else if (x_hor[ty] == 3 || x_vert[tx] == 3)
			printf("X won\n");
		else if (y_hor[ty] == 3 || y_vert[tx] == 3)
			printf("O won\n");
		else if (x_di1 == 4 || x_di2 == 4)
			printf("X won\n");
		else if (tx != -1 && tx == ty && x_di1 == 3)
			printf("X won\n");
		else if (tx != -1 && tx + ty == 3 && x_di2 == 3)
			printf("X won\n");
		else if (y_di1 == 4 || y_di2 == 4)
			printf("O won\n");
		else if (tx != -1 && tx == ty && y_di1 == 3)
			printf("O won\n");
		else if (tx != -1 && tx + ty == 3 && y_di2 == 3)
			printf("O won\n");
		else if (dot == 0)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
}