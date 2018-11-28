#include <iostream>
#include <cstdio>


using namespace std;
enum State{Xwon, Owon, Draw, Gamehasnotcompleted};

const short int size = 4;
char Bord[size][size] = {};
char BordX[size][size] = {};
char BordO[size][size] = {};

void createBord(char player, char BordT[size][size])
{
	char pl = 0;
	if (player == 'X') pl = 1;
	else pl = -1;
	for(short int i = 0; i < size; i++)
	{
		for(short int j = 0; j < size; j++)
		{
			switch(Bord[i][j])
			{
			case 'X': BordT[i][j] = 1;
				break;
			case 'O': BordT[i][j] = -1;
				break;
			case '.': BordT[i][j] = 0;
				break;
			case 'T': BordT[i][j] = pl;
				break;
			}
		}
	}
}

bool isWinnerT(char player, char bord[size][size])
{
	bool res = false;
	if(player == 'X')
	{
		if(
			bord[0][0] + bord[0][1] + bord[0][2] + bord[0][3] == 4 ||
			bord[1][0] + bord[1][1] + bord[1][2] + bord[1][3] == 4 ||
			bord[2][0] + bord[2][1] + bord[2][2] + bord[2][3] == 4 ||
			bord[3][0] + bord[3][1] + bord[3][2] + bord[3][3] == 4 ||

			bord[0][0] + bord[1][0] + bord[2][0] + bord[3][0] == 4 ||
			bord[0][1] + bord[1][1] + bord[2][1] + bord[3][1] == 4 ||
			bord[0][2] + bord[1][2] + bord[2][2] + bord[3][2] == 4 ||
			bord[0][3] + bord[1][3] + bord[2][3] + bord[3][3] == 4 ||

			bord[0][0] + bord[1][1] + bord[2][2] + bord[3][3] == 4 ||
			bord[0][3] + bord[1][2] + bord[2][1] + bord[3][0] == 4
			)
			res = true;
	} 
	else
	{
		if(
			bord[0][0] + bord[0][1] + bord[0][2] + bord[0][3] == -4 ||
			bord[1][0] + bord[1][1] + bord[1][2] + bord[1][3] == -4 ||
			bord[2][0] + bord[2][1] + bord[2][2] + bord[2][3] == -4 ||
			bord[3][0] + bord[3][1] + bord[3][2] + bord[3][3] == -4 ||

			bord[0][0] + bord[1][0] + bord[2][0] + bord[3][0] == -4 ||
			bord[0][1] + bord[1][1] + bord[2][1] + bord[3][1] == -4 ||
			bord[0][2] + bord[1][2] + bord[2][2] + bord[3][2] == -4 ||
			bord[0][3] + bord[1][3] + bord[2][3] + bord[3][3] == -4 ||

			bord[0][0] + bord[1][1] + bord[2][2] + bord[3][3] == -4 ||
			bord[0][3] + bord[1][2] + bord[2][1] + bord[3][0] == -4
			)
			res = true;
	}

	return res;
}

int main()
{
	short int T;
	char tmp = ' ';
	FILE *f;
	f = fopen("large.in", "r");
	FILE *fout = fopen("out.out", "w+");

	State game = Draw;
	bool hasDots = false;

	fscanf(f, "%hi", &T);
	for(short int t = 1; t <= T; t++)
	{
		fscanf(f,"%c", &tmp);
		for(short int i = 0; i < size; i++)
		{
			for(short int j = 0; j < size; j++)
			{
				fscanf(f,"%c", &Bord[i][j]);	
			}
			fscanf(f,"%c", &tmp);
		}

		for(int k = 0; k < size; k++)
			for(int l = 0; l < size; l++) if (Bord[k][l] == '.') { hasDots = true; break;}

			createBord('X', BordX);
			createBord('O', BordO);

			if(isWinnerT('X', BordX)) 
			{
				game = Xwon;
			}else{
				if(isWinnerT('O', BordO))
				{
					game = Owon;
				}else 
				{
					if(!hasDots) 
					{
						game = Draw;
					} else { game = Gamehasnotcompleted;}
				}
			}

			fprintf(fout,"Case #%hi: ", t);
			switch (game)
			{
			case Xwon: fprintf(fout,"X won\n");
				break;
			case Owon: fprintf(fout,"O won\n");
				break;
			case Draw: fprintf(fout,"Draw\n");
				break;
			case Gamehasnotcompleted: fprintf(fout,"Game has not completed\n");
				break;
			}
			hasDots = false;
			game = Draw;
	}
	return 0;
}