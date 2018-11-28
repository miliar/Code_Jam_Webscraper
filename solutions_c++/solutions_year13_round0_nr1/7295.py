#include <iostream>
using namespace std;

char board[4][4];

int main(int argc, char *argv[]) {
	int ncases;
	cin >> ncases;
	
	for(int ncase = 1; ncase <= ncases; ++ ncase)
	{
		for(int i = 0; i < 4; ++ i)
			for(int j = 0; j < 4; ++ j)
				cin >> board[i][j];
		
		bool winner = false;
		char ganador;
		//Busco fila
		for(int i = 0; i < 4 && !winner; ++ i)
		{
			ganador = board[i][0];
			bool fila = true;
			for(int j = 1; j < 4 && fila; ++ j)
			{
				if(ganador == 'T')
					ganador = board[i][j];
				else if(board[i][j] != 'T' && (ganador != board[i][j] || ganador == '.')) 
					fila = false;
			}
			if (fila)
				winner = true;
		}
		
		//Busco columna
		for(int j = 0; j < 4 && !winner; ++j)
		{
			ganador = board[0][j];
			bool col = true;
			for(int i = 1; i < 4 && col; ++ i)
			{
				if(ganador == 'T')
					ganador = board[i][j];
				else if(board[i][j] != 'T' && (board[i][j] != ganador || ganador == '.'))
					col = false;
			}
			if (col)
				winner = true;
		}
		
		//Busco diagonal
		if(!winner)
		{
			ganador = board[0][0];
			bool diag = true;
			for(int i = 1; i < 4 && diag; ++ i)
			{
				if(ganador == 'T')
					ganador = board[i][i];
				else if(board[i][i] != 'T' && (board[i][i] != ganador || ganador == '.'))
					diag = false;
			}
			if(diag)
			{
				winner = true;
			}
			else
			{
				ganador = board[0][3];
				bool diag = true;
				for(int i = 1; i < 4 && diag; ++ i)
				{
					if(ganador == 'T')
						ganador = board[i][3-i];
					else if(board[i][3-i] != 'T' && (board[i][3-i] != ganador || ganador == '.'))
						diag = false;
				}
				if(diag)
				{
					winner = true;
				}
			}
		}
		cout << "Case #" << ncase << ": ";
		if(winner)
			cout << ganador << " won" << endl;
		else 
		{
			bool punto = false;
			for(int i = 0; i < 4 && !punto; i ++)
				for(int j = 0; j < 4 && !punto; ++ j)
					if(board[i][j] == '.') punto = true;
			if(punto)
				cout << "Game has not completed" << endl;
			else
				cout << "Draw" << endl;
		}

	}
	
	return 0;
}

