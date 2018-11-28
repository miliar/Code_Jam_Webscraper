#include <cstdio>
#include <cstring>

char game[4][5];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Test;
	scanf("%d", &Test);
	int i, j;
	int X, O, T;
	int case_num = 0;
	bool flag = false;
	while ((++case_num) <= Test)
	{
		flag = false;
		for (i = 0; i < 4; ++i)
			scanf("%s", game[i]);
		for (i = 0; i < 4; ++i)
		{
			X = O = T = 0;
			for (j = 0; j < 4; ++j)
				if (game[i][j] == 'X')
					++X;
				else if (game[i][j] == 'O')
					++O;
				else if (game[i][j] == 'T')
					++T;
			if (O == 0 && X + T == 4)
			{
				flag = true;
				printf("Case #%d: X won\n", case_num);
				break;
			}
			if (X == 0 && O + T == 4)
			{
				flag = true;
				printf("Case #%d: O won\n", case_num);
				break;
			}
			X = O = T = 0;
			for (j = 0; j < 4; ++j)
				if (game[j][i] == 'X')
					++X;
				else if (game[j][i] == 'O')
					++O;
				else if (game[j][i] == 'T')
					++T;
			if (O == 0 && X + T == 4)
			{
				flag = true;
				printf("Case #%d: X won\n", case_num);
				break;
			}
			if (X == 0 && O + T == 4)
			{
				flag = true;
				printf("Case #%d: O won\n", case_num);
				break;
			}
		}
		if (flag)
			continue;
		X = O = T = 0;
		for (i = 0; i < 4; ++i)
			if (game[i][i] == 'X')
				++X;
			else if (game[i][i] == 'O')
				++O;
			else if (game[i][i] == 'T')
				++T;
		if (O == 0 && X + T == 4)
		{
			printf("Case #%d: X won\n", case_num);
			continue;
		}
		if (X == 0 && O + T == 4)
		{
			printf("Case #%d: O won\n", case_num);
			continue;
		}
		X = O = T = 0;
		for (i = 0; i < 4; ++i)
			if (game[i][3 - i] == 'X')
				++X;
			else if (game[i][3 - i] == 'O')
				++O;
			else if (game[i][3 - i] == 'T')
				++T;
		if (O == 0 && X + T == 4)
		{
			printf("Case #%d: X won\n", case_num);
			continue;
		}
		if (X == 0 && O + T == 4)
		{
			printf("Case #%d: O won\n", case_num);
			continue;
		}
		flag = true;
		for (i = 0; i < 4 && flag; ++i)
			for (j = 0; j < 4 && flag; ++j)
				if (game[i][j] == '.')
				{
					flag = false;
					printf("Case #%d: Game has not completed\n", case_num);
				}
		if (flag)
			printf("Case #%d: Draw\n", case_num);
	}
	return 0;
}
