#include <iostream>
#include <fstream>
using namespace std;

class tik
{
	char game[4][4];
    public:
	tik(string a)
	{
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				game[i][j] = a[4*i+j];
			}
		}
	}
	string solve()
	{
		int numOfX = 0;
		int numOfO = 0;
		int numOfT = 0;
		int numOf = 0;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if( game[i][j] == '.') {numOf++; break;}
				if( game[i][j] == 'X') numOfX++;
				if( game[i][j] == 'O') numOfO++;
				if( game[i][j] == 'T') numOfT++;
			}
			if( numOfX == 4 || (numOfX == 3 && numOfT == 1)) return "X won";
			if( numOfO == 4 || (numOfO == 3 && numOfT == 1)) return "O won";
			numOfX = 0; numOfO = 0; numOfT = 0;
		}
		for(int i = 0; i < 4; i++)
                {
                        for(int j = 0; j < 4; j++)
                        {
                                if( game[j][i] == '.') {numOf++;break;}
                                if( game[j][i] == 'X') numOfX++;
                                if( game[j][i] == 'O') numOfO++;
                                if( game[j][i] == 'T') numOfT++;
                        }
                        if( numOfX == 4 || (numOfX == 3 && numOfT == 1)) return "X won";
                        if( numOfO == 4 || (numOfO == 3 && numOfT == 1)) return "O won";
                	numOfX = 0; numOfO = 0; numOfT = 0;
		}
		for(int i = 0; i < 4; i++)
		{
			if(game[i][i] == '.') {numOf++;break;}
			if(game[i][i] == 'X') numOfX++;
			if(game[i][i] == 'O') numOfO++;
			if(game[i][i] == 'T') numOfT++;
		}
		if( numOfX == 4 || (numOfX == 3 && numOfT == 1)) return "X won";
                if( numOfO == 4 || (numOfO == 3 && numOfT == 1)) return "O won";
                numOfX = 0; numOfO = 0; numOfT = 0;
		for(int i = 0; i < 4; i++)
                {
                        if(game[i][3-i] == '.') {numOf++;break;}
                        if(game[i][3-i] == 'X') numOfX++;
                        if(game[i][3-i] == 'O') numOfO++;
                        if(game[i][3-i] == 'T') numOfT++;
                }
		if( numOfX == 4 || (numOfX == 3 && numOfT == 1)) return "X won";
                if( numOfO == 4 || (numOfO == 3 && numOfT == 1)) return "O won";

		if( numOf > 0) return "Game has not completed";
		if( numOf == 0) return "Draw";
	}
};

int main(int argc, char *argv[])
{
	int sizeOfGame;
	cin >> sizeOfGame;

	tik* games[sizeOfGame];

	char indice;
	for(int i = 0; i < sizeOfGame; i++)
	{
		string a = "................";
		for(int j = 0; j < 16; j++)
		{
			cin >> indice;
			a[j] = indice;
		}
		games[i] = new tik(a);
	}

	for(int i = 0; i < sizeOfGame; i++)
	{
		cout << "Case #" << i+1 << ": " << games[i]->solve() << endl;
		delete games[i];
	}
}
