#include <cstdio>
#include <cstring>

using namespace std;

#define GANO 1
#define PERDIO 0
#define DESCONTINUADO 2

short int gano(char tablero[4][5], char jugador){
	short int vertical, horizontal;
	bool libres = false;	
	int j;
	for (int i = 0; i < 4; i++)
	{
		horizontal = GANO;
		for (j = 0; j < 4; j++)
		{
			if(tablero[i][j] == '.')libres = true;
			if(tablero[i][j] != jugador && tablero[i][j] != 'T'){
				horizontal = PERDIO;
			}
		}
		if(horizontal == GANO){ 
			//printf("Gano %c en la fila %d", jugador, j+1);
			return horizontal;}
	}
	for (int i = 0; i < 4; i++){
		vertical = GANO;
		for (j = 0; j < 4; j++){
			if(tablero[j][i] != jugador && tablero[j][i] != 'T'){
				vertical = PERDIO;
			}
		}
		if(vertical == GANO){ 
			//printf("Gano %c en la columna %d", jugador, j+1);
			return vertical;}
	}
	vertical = horizontal = GANO;
	for (int i = 0, j = 3; i < 4 && j >= 0 ; i++, j--)
	{
		if(tablero[i][i] != jugador && tablero[i][i] != 'T') vertical = PERDIO;
		if(tablero[i][j] != jugador && tablero[i][j] != 'T') horizontal = PERDIO;
	}
	if(vertical == GANO){ //printf("Gano %c diagonalmente", jugador);
		return GANO;}
	if(horizontal == GANO) return GANO;
	if(libres) return DESCONTINUADO;
	return PERDIO;
	
}

int main(){
	int T;
	char tablero[4][5];
	short int oWon, xWon;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			scanf("%s", tablero[j]);
			
		}
		oWon = gano(tablero, 'O');
		xWon = gano(tablero, 'X');
		printf("Case #%d: ", i);
		if(oWon == GANO) printf("O won\n");
		else if(xWon == GANO) printf("X won\n");
		else if(oWon == DESCONTINUADO) printf("Game has not completed\n");
		else printf("Draw\n");	
	}
	
	return 0;
}
