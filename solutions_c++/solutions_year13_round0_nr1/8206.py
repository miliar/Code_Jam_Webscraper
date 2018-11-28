#include<cstdio>
char tab[5][5];
void spr_wygrana(int case_numer)
{
	bool czy_x = false;
	bool czy_y = false;
	bool czy_puste = false;
	//po wierszach
	for(int w = 0; w < 4; w++)
	{
		int zaw_x = 0;
		int zaw_y = 0;
		int puste = 0;
		for(int k = 0; k < 4; k++)
		{
			if(tab[w][k] == 'X' || tab[w][k] == 'T')
				++zaw_x;
			if(tab[w][k] == 'O' || tab[w][k] == 'O')
				++zaw_y;
			if(tab[w][k] == '.')
				++puste;
		}
		if(zaw_x == 4)
			czy_x = true;
		if(zaw_y == 4)
			czy_y = true;
		if(puste > 0)
			czy_puste = true;
	}
	// po kolumnach
	for(int w = 0; w < 4; w++)
	{
		int zaw_x = 0;
		int zaw_y = 0;
		for(int k = 0; k < 4; k++)
		{
			if(tab[k][w] == 'X' || tab[k][w] == 'T')
				++zaw_x;
			if(tab[k][w] == 'O' || tab[k][w] == 'T')
				++zaw_y;
		}
		if(zaw_x == 4)
			czy_x = true;
		if(zaw_y == 4)
			czy_y = true;
	}
	//po przekatnych
	int zaw_x = 0;
	int zaw_y = 0;
	for(int i = 0; i < 4; i++)
	{
		if(tab[i][i] == 'X' || tab[i][i] == 'T')
			++zaw_x;
		if(tab[i][i] == 'O' || tab[i][i] == 'T')
			++zaw_y;
	}
	if(zaw_x == 4)
		czy_x = true;
	if(zaw_y == 4)
		czy_y = true;
	//druga
	zaw_x = 0;
	zaw_y = 0;
	for(int i = 3; i >= 0; i--)
	{
		if(tab[3 - i][i] == 'X' || tab[3 - i][i] == 'T')
			++zaw_x;
		if(tab[3 - i][i] == 'O' || tab[3 - i][i] == 'T')
			++zaw_y;
	}
	if(zaw_x == 4)
		czy_x = true;
	if(zaw_y == 4)
		czy_y = true;
	//Draw
	if(czy_x == true && czy_y == true)
		printf("Case #%d: Draw\n", case_numer);
	else // X won
	if(czy_x == true)
		printf("Case #%d: X won\n", case_numer);
	else //
	if(czy_y == true)
		printf("Case #%d: O won\n", case_numer);
	else
	if(czy_puste == true)
		printf("Case #%d: Game has not completed\n", case_numer);
	else
		printf("Case #%d: Draw\n", case_numer);
}
int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		int wier = 0;
		while(wier < 4)
		{
			int kol = 0;
			while(kol < 4)
			{
				char znak;
				scanf("%c", &znak);
				if(znak == 'X' || znak == 'O' || znak == '.' || znak == 'T')
				{
					tab[wier][kol] = znak;
					++kol;
				}
			}
			++wier;
		}
	//	scanf("\n");
		spr_wygrana(i + 1);
		/*for(int w = 0; w < 4; w++)
		{
			for(int k = 0; k < 4; k++)
				printf("%c", tab[w][k]);
			printf("\n");
		}*/
	}
	return 0;
}