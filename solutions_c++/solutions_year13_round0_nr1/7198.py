#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int casos, i, j, k, X, O, T, puntos;
	string board[4], answer;
	cin >> casos;
	for(i = 1; i <= casos; i++)
	{
		// Lectura
		for(j = 0; j < 4; j++)
			cin >> board[j];
		
		puntos = X = O = T = 0;
		for(j = 0; j < 4; j++)
		{
			// Revisar filas
			for(k = 0; k < 4; k++)
			{
				if(board[j][k] == 'X')
					X++;
				else if(board[j][k] == 'O')
					O++;
				else if(board[j][k] == 'T')
					T++;
				else
				{
					puntos++;
					break;
				}
			}
			// Revisar si hay elementos de ambos jugadores o si hay linea completa
			if((X > 0) && (O > 0))
				X = O = 0;
			if(((X+T) == 4) || ((O+T) == 4))
				break;
			X = O = T = 0;
			// Revisar columnas
			for(k = 0; k < 4; k++)
			{
				if(board[k][j] == 'X')
					X++;
				else if(board[k][j] == 'O')
					O++;
				else if(board[k][j] == 'T')
					T++;
				else
					break;
			}
			// Revisar si hay elementos de ambos jugadores o si hay linea completa
			if((X > 0) && (O > 0))
				X = O = T = 0;
			if(((X+T) == 4) || ((O+T) == 4))
				break;
			X = O = T = 0;
		}
		// Revisar diagonal izq
		if(((X+T) != 4) && ((O+T) != 4))
		{
			X = O = T = 0;
			for(j =0; j < 4; j++)
				for(k = 0; k < 4; k++)
					if(j == k)
						if(board[k][j] == 'X')
							X++;
						else if(board[k][j] == 'O')
							O++;
						else if(board[k][j] == 'T')
							T++;
						else
							break;
		}
		// Revisar diagonal der
		if(((X+T) != 4) && ((O+T) != 4))
		{
			X = O = T = 0;
			for(j = 0; j < 4; j++)
				for(k = 0; k < 4; k++)
					if(j == k)
						if(board[k][3-j] == 'X')
							X++;
						else if(board[k][3-j] == 'O')
							O++;
						else if(board[k][3-j] == 'T')
							T++;
						else
							break;
		}
		// Output
		if((X+T) == 4)
			answer = "X won";
		else if((O+T) == 4)
			answer = "O won";
		else if(puntos > 0)
			answer = "Game has not completed";
		else
			answer = "Draw";
		cout << "Case #" << i << ": " << answer << endl;
	}
}
