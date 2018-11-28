#include <cstdio>

using namespace std;

int T, t;

char B[5][5];

bool spr_pion(char g)
{
	int i, j;
	for(i = 0; i < 4; i++)
	{
		if(
			(B[0][i] == g || B[0][i] == 'T') &&
			(B[1][i] == g || B[1][i] == 'T') &&
			(B[2][i] == g || B[2][i] == 'T') &&
			(B[3][i] == g || B[3][i] == 'T')
			)
		{
			return true;
		}
	}
	return false;
}

bool spr_poziom(char g)
{
	int i, j;
	for(i = 0; i < 4; i++)
	{
		if(
			(B[i][0] == g || B[i][0] == 'T') &&
			(B[i][1] == g || B[i][1] == 'T') &&
			(B[i][2] == g || B[i][2] == 'T') &&
			(B[i][3] == g || B[i][3] == 'T')
			)
		{
			return true;
		}
	}
	return false;
}

bool spr_przek(char g)
{
	if(
		(B[0][0] == g || B[0][0] == 'T') &&
		(B[1][1] == g || B[1][1] == 'T') &&
		(B[2][2] == g || B[2][2] == 'T') &&
		(B[3][3] == g || B[3][3] == 'T')
		)
	{
		return true;
	}

	if(
		(B[0][3] == g || B[0][3] == 'T') &&
		(B[1][2] == g || B[1][2] == 'T') &&
		(B[2][1] == g || B[2][1] == 'T') &&
		(B[3][0] == g || B[3][0] == 'T')
		)
	{
		return true;
	}

	return false;
}

bool jest_kropka()
{
	int i, j;
	for(i = 0; i < 4; i++)
	{
		for(j = 0; j < 4; j++)
		{
			if(B[i][j] == '.')
			{
				return true;
			}
		}
	}
	return false;
}

int main()
{
	scanf("%d", &T);

	for(t = 1; t <= T; t++)
	{
		scanf("%s\n%s\n%s\n%s\n", B[0], B[1], B[2], B[3]);
		printf("Case #%d: %s\n", t,
				(spr_pion('X') || spr_poziom('X') || spr_przek('X')) ? "X won"
					: (spr_pion('O') || spr_poziom('O') || spr_przek('O')) ? "O won"
							: (!jest_kropka()) ? "Draw" : "Game has not completed"
				);
	}

	return 0;
}
