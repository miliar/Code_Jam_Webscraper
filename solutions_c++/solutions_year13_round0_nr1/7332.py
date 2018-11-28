#include <iostream>
#include <fstream>

using namespace std;
string v[4];
bool hayVacio;
string solve(){
	char X = 'X', O = 'O';
	hayVacio = false;

	for(int i = 0; i < 4; i++){
		bool filaX = true, colX = true;
		bool filaO = true, colO = true;
		for(int j = 0; j < 4; j++){
			filaX &= (v[i][j]==X || v[i][j]=='T');
			colX  &= (v[j][i]==X || v[j][i]=='T');
			filaO &= (v[i][j]==O || v[i][j]=='T');
			colO  &= (v[j][i]==O || v[j][i]=='T');
			if(v[i][j]=='.' || v[j][i] == '.')hayVacio = true;
		}
		if(filaX || colX)return "X won";
		if(filaO || colO)return "O won";
	}

	bool sX = true, bsX = true;
	bool sO = true, bsO = true;
	for(int i = 0; i < 4; i++){
		bsX &= (v[i][i]==X || v[i][i]=='T');
		sX &= (v[i][3-i]==X || v[i][3-i]=='T');

		bsO &= (v[i][i]==O || v[i][i]=='T');
		sO &= (v[i][3-i]==O || v[i][3-i]=='T');
	}
	if(sX || bsX)return "X won";
	if(sO || bsO)return "O won";
	if(hayVacio)return "Game has not completed";
	return "Draw";
}
int main() {
	//ifstream cin ("input.txt");
	//ofstream cout ("output.txt");
	int t;
	cin  >> t;
	for(int caso = 1; caso <= t; caso++){

		for(int i = 0; i < 4; i++)cin >> v[i];

		cout << "Case #" << caso << ": " << solve() << endl;
	}
	return 0;
}



