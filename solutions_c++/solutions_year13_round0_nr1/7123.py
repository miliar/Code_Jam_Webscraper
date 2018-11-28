#include <iostream>
#include <string>

using namespace std;

int main() {
	string tab[4];
	int T, x, t, o, ge;
	bool xwin, owin;
	
	cin >> T;
	for (int k = 0; k < T; k++) {
		ge = 0; xwin = false; owin = false;
		for (int i = 0; i < 4; i++)
			cin >> tab[i];
		
		//Reviso columnas	
		for (int i = 0; i < 4; i++) {
			x = 0; t = 0; o = 0;
			for (int j = 0; j < 4; j++) {
				if ( tab[i][j] == 'X' ) x++;
				else if ( tab[i][j] == 'O' ) o++;
				else if ( tab[i][j] == 'T' ) t++;
				else ge++;
			}
			if ( x+t == 4 ) xwin = true;
			else if ( o+t == 4 ) owin = true;
		}
		//Reviso filas
		for (int j = 0; j < 4; j++) {
			x = 0; t = 0; o = 0;
			for (int i = 0; i < 4; i++) {
				if ( tab[i][j] == 'X' ) x++;
				else if ( tab[i][j] == 'O' ) o++;
				else if ( tab[i][j] == 'T' ) t++;
				else ge++;
			}
			if ( x+t == 4 ) xwin = true;
			else if ( o+t == 4 ) owin = true;
		}
		//Reviso diagonales
		x = 0; t = 0; o = 0;
		for (int i = 0; i < 4; i++) {
			if ( tab[i][i] == 'X' ) x++;
			else if ( tab[i][i] == 'O' ) o++;
			else if ( tab[i][i] == 'T' ) t++;
			else ge++;
		}
		if ( x+t == 4 ) xwin = true;
		else if ( o+t == 4 ) owin = true;
		
		x = 0; t = 0; o = 0;
		for (int i = 0; i < 4; i++) {
			if ( tab[3-i][i] == 'X' ) x++;
			else if ( tab[3-i][i] == 'O' ) o++;
			else if ( tab[3-i][i] == 'T' ) t++;
			else ge++;
		}
		if ( x+t == 4 ) xwin = true;
		else if ( o+t == 4 ) owin = true;
		
		//Analizo resultados
		if ( xwin )
			cout << "Case #" << k+1 << ": X won" << endl;
		else if ( owin )
			cout << "Case #" << k+1 << ": O won" << endl;
		else if ( ge == 0 )
			cout << "Case #" << k+1 << ": Draw" << endl;
		else
			cout << "Case #" << k+1 << ": Game has not completed" << endl;
	
	}
	
	return 0;
}
				
		
	
	
