#include <stdio.h>
#include <string>
#include <iostream>



/*


Problem

Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in 
one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts 
her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.

After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her 
symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the 
fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning 
positions.

Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), 
describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from 
are:

"X won" (the game is over, and X won)
"O won" (the game is over, and O won)
"Draw" (the game is over, and it ended in a draw)
"Game has not completed" (the game is not over yet)

If there are empty cells, and the game is not over, you should output "Game has not completed", even if the outcome of the 
game is inevitable.

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of 4 lines with 4 
characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an 
empty line.
Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of 
the statuses given above. Make sure to get the statuses exactly right. When you run your code on the sample input, it should 
create the sample output exactly, including the "Case #1: ", the capital letter "O" rather than the number "0", and so on.

Limits

The game board provided will represent a valid state that was reached through play of the game Tic-Tac-Toe-Tomek as 
described above.

Small dataset

1 ≤ T ≤ 10.
Large dataset

1 ≤ T ≤ 1000.
Sample

Input

Output

6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O

Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won

Note

Although your browser might not render an empty line after the last test case in the sample input, in a real input file 
there would be one.


*/

using namespace std;

char tablero[4][4];
int x = 0, y = 0;

string msgs[] = {
	"X won",
	"O won",
	"Draw",
	"Game has not completed",
};

FILE *escribir = fopen("C:\\Proyecto Program 2\\output.txt", "w");


bool checkTableroEstaFull()
{
	int cantLetras = 0;
	for (int xx = 0; xx < 4; xx++)
	{
		for (int yy = 0; yy < 4; yy++)
		{
			if (tablero[xx][yy] == 'X' || tablero[xx][yy] == 'O' || tablero[xx][yy] == 'T')
				cantLetras++;
		}
	}
	if (cantLetras == 16)
		return true;
	else
		return false;
}

bool estaFull()
{
	int cantLetras = 0;
	for (int xx = 0; xx < 4; xx++)
	{
		for (int yy = 0; yy < 4; yy++)
		{
			if (tablero[xx][yy] == 'X' || tablero[xx][yy] == 'O' || tablero[xx][yy] == 'T' || tablero[xx][yy] == '.')
				cantLetras++;
		}
	}
	if (cantLetras == 16)
		return true;
	else
		return false;
}

int diagonalPositiva()
{
	int aciertosX = 0, aciertosO = 0;
	for (int i = 0; i < 4; i++)
	{
		if (tablero[i][i] == 'X' || tablero[i][i] == 'T')
			aciertosX++;
		if (tablero[i][i] == 'O' || tablero[i][i] == 'T')
			aciertosO++;		
	}
	if (aciertosX == 4)
		return 0; // Id en msgs
	else if (aciertosO == 4)
		return 1;
	else
		return -1;
}

int diagonalNegativa()
{
	int aciertosX = 0, aciertosO = 0;
	int xx = 3;
	int yy = 0;
	while (xx >= 0 && yy < 4)
	{
		if (tablero[xx][yy] == 'X' || tablero[xx][yy] == 'T')
			aciertosX++;
		if (tablero[xx][yy] == 'O' || tablero[xx][yy] == 'T')
			aciertosO++;
		xx--;
		yy++;
	}

	if (aciertosX == 4)
		return 0; // Id en msgs
	else if (aciertosO == 4)
		return 1;
	else
		return -1;
}

int verticales()
{
	int aciertosX = 0, aciertosO = 0;

	for (int xx = 0; xx < 4; xx++)
	{
		for (int yy = 0; yy < 4; yy++)
		{
			if (tablero[xx][yy] == 'X' || tablero[xx][yy] == 'T')
				aciertosX++;
			if (tablero[xx][yy] == 'O' || tablero[xx][yy] == 'T')
				aciertosO++;
		}
		if (aciertosX == 4 || aciertosO == 4)
			break;
		else
		{
			aciertosX = 0;
			aciertosO = 0;
		}
	}

	if (aciertosX == 4)
		return 0; // Id en msgs
	else if (aciertosO == 4)
		return 1;
	else
		return -1;
}

int horizontales()
{
	int aciertosX = 0, aciertosO = 0;

	for (int yy = 0; yy < 4; yy++)
	{
		for (int xx = 0; xx < 4; xx++)
		{
			if (tablero[xx][yy] == 'X' || tablero[xx][yy] == 'T')
				aciertosX++;
			if (tablero[xx][yy] == 'O' || tablero[xx][yy] == 'T')
				aciertosO++;
		}
		if (aciertosX == 4 || aciertosO == 4)
			break;
		else
		{
			aciertosX = 0;
			aciertosO = 0;
		}
	}

	if (aciertosX == 4)
		return 0; // Id en msgs
	else if (aciertosO == 4)
		return 1;
	else
		return -1;
}

void reiniciarTablero()
{
	for (int xx = 0; xx < 4; xx++)
	{
		for (int yy = 0; yy < 4; yy++)
		{
			tablero[xx][yy] = NULL;
		}
	}
	x = 0;
	y = 0;
	//printf("Tablero reiniciado");
}

void imprimirTablero()
{
	for (int yy = 0; yy < 4; yy++)
	{
		for (int xx = 0; xx < 4; xx++)
		{
			printf("%c -- ", tablero[xx][yy]);
		}
		printf("\n");
	}
	system("PAUSE");
}

void darSolucion(int caso)
{
	int resp;
	fprintf(escribir, "Case #%d: ", caso);
	resp = diagonalPositiva();

	if (resp != -1)
	{		
		switch (resp)
		{
		case 0:
			fprintf(escribir, "X won\n");
			break;
		case 1:
			fprintf(escribir, "O won\n");
			break;
		}
		reiniciarTablero();
		return;
	}

	resp = diagonalNegativa();
	if (resp != -1)
	{
		//cout << msgs[resp] << endl;
		switch (resp)
		{
		case 0:
			fprintf(escribir, "X won\n");
			break;
		case 1:
			fprintf(escribir, "O won\n");
			break;
		}
		reiniciarTablero();
		return;
	}

	resp = verticales();
	if (resp != -1)
	{
		switch (resp)
		{
		case 0:
			fprintf(escribir, "X won\n");
			break;
		case 1:
			fprintf(escribir, "O won\n");
			break;
		}
		reiniciarTablero();
		return;
	}

	resp = horizontales();
	if (resp != -1)
	{
		switch (resp)
		{
		case 0:
			fprintf(escribir, "X won\n");
			break;
		case 1:
			fprintf(escribir, "O won\n");
			break;
		}
		reiniciarTablero();
		return;
	}

	/* Si nadie gano.. entonces */

	if (checkTableroEstaFull())
		fprintf(escribir, "Draw\n");
		//cout << msgs[2] << endl;
	else
		fprintf(escribir, "Game has not completed\n");
		//cout << msgs[3] << endl;

	reiniciarTablero();
	return;

}

void introducirEnTablero(char c)
{
	if (c == 'O' || c == 'X' || c == '.' || c == 'T')
	{
		tablero[x][y] = c;
		x++;
		if (x > 3)
		{
			y++;
			x = 0;
		}	
	}	
}




void leerInfo()
{
	FILE *archivo;
	archivo = fopen("C:\\Proyecto Program 2\\Test.txt", "r");
	char act;
	int numDeCasos;	

	if (archivo)
	{

		fscanf(archivo, "%d", &numDeCasos);
		//fscanf(archivo, "%c", &act); // Leer mierda
		for (int i = 1; i <= numDeCasos; i++)
		{			
			//cout << endl << endl << endl;
			while (!estaFull())
			{					
				fscanf(archivo, "%c", &act);					
				introducirEnTablero(act);				
			}
			//imprimirTablero();
			//fscanf(archivo, "%c", &act); // Leer linea vacia?
			darSolucion(i);
		}

	}
}


void main()
{
	leerInfo();
	fclose(escribir);
}