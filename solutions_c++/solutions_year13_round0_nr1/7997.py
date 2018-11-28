#include <iostream>
using namespace std;

char tablero[4][4];
int t, ganador;

int estado(char J) {
	int posx,posy;
	int cont = 0;

	for(int y=0;y<4;y++){
		for(int x=0;x<4;x++){
			if(tablero[y][x]=='T'){
				tablero[y][x] = J;
				posx = x;
				posy =y;
			}
			if(tablero[y][x]=='.')
				cont++;
		}
	}

	for(int y=0;y<4;y++){
		if((tablero[y][0]==J) && (tablero[y][1]==J) && (tablero[y][2]==J) && (tablero[y][3]==J)){
			if (J == 'X') {
				tablero[posy][posx] = 'T';
				return 1;
			}
			else {
				tablero[posy][posx] = 'T';
				return 2;
			}
		}
	}
	for(int x=0;x<4;x++){
		if((tablero[0][x]==J) && (tablero[1][x]==J) && (tablero[2][x]==J) && (tablero[3][x]==J)){
			if (J == 'X') {
				tablero[posy][posx] = 'T';
				return 1;
			}
			else {
				tablero[posy][posx] = 'T';
				return 2;
			}		}
	}

	if((tablero[0][0]==J) && (tablero[1][1]==J) && (tablero[2][2]==J) && (tablero[3][3]==J)){
		if (J == 'X') {
			tablero[posy][posx] = 'T';
			return 1;
		}
		else {
			tablero[posy][posx] = 'T';
			return 2;
		}
	}
	if((tablero[0][3]==J) && (tablero[1][2]==J) && (tablero[2][1]==J) && (tablero[3][0]==J)){
		if (J == 'X') {
			tablero[posy][posx] = 'T';
			return 1;
		}
		else {
			tablero[posy][posx] = 'T';
			return 2;
		}
	}

	if(cont > 0) {
		tablero[posy][posx] = 'T';
		return 0;
	}

	tablero[posy][posx] = 'T';
	return 3;
}

int main() {
	cin >> t;

	for(int a=1;a<=t;a++) {
		ganador = 0;
		for(int y=0;y<4;y++){
			for(int x=0;x<4;x++){
				cin >> tablero[y][x];
			}
		}

		ganador = estado('X');
		if (ganador==1) {
			cout << "Case #" << a << ": X won" << endl;
		}
		else {
			ganador = estado('O');
			if(ganador==2) {
				cout << "Case #" << a << ": O won" << endl;
			}
			else if(ganador==3) {
				cout << "Case #" << a << ": Draw" << endl;
			}
			else {
				cout << "Case #" << a << ": Game has not completed" << endl;
			}
		}

		cin.get();
	}


	return 0;
}
