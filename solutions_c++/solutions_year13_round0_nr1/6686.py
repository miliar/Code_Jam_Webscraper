#include<fstream>

using namespace std;


void main(){
	int stanje = 0; // 0-game not completed, 1 - X, 2 - O, 3 - draw;
	int n, counter;
	char tabla[4][4],c;
	ifstream ulaz;
	ulaz.open("TTTT_in.txt");
	ulaz>>n;
	ofstream izlaz;
	izlaz.open("A-small-attempt0.out");

	for(counter = 0; counter<n; counter++){
		for(int i = 0; i<4; i++){
			for(int j = 0; j<4; j++){
				ulaz>>tabla[i][j];
			}
		}//ucitavanje
		//ulaz>>c;

		stanje = 1;
		for(int i = 0; i<4; i++){
			if(tabla[i][i]!='X' && tabla[i][i]!='T') stanje = 0;
		}//X - glavna dijagonala

		if (stanje == 1) {
			izlaz<<"Case #"<<counter+1<<": X won\n"; 
			continue;
		}

		stanje = 1;
		for(int i = 0; i<4; i++){
			if(tabla[i][3-i]!='X' && tabla[i][3-i]!='T') stanje = 0;
		}//X - sporedna dijagonala

		if (stanje == 1) {
			izlaz<<"Case #"<<counter+1<<": X won\n"; 
			continue;
		}


		for(int j = 0; j< 4; j++){
			stanje = 1;
			for(int i = 0; i<4; i++){
				if(tabla[j][i]!='X' && tabla[j][i]!='T') stanje = 0;
			}//X - vrste

			if (stanje == 1) {
				izlaz<<"Case #"<<counter+1<<": X won\n"; 
				break;
			}

			stanje = 1;
			for(int i = 0; i<4; i++){
				if(tabla[i][j]!='X' && tabla[i][j]!='T') stanje = 0;
			}//X - kolone

			if (stanje == 1) {
				izlaz<<"Case #"<<counter+1<<": X won\n"; 
				break;
			}
		}


		if(stanje == 1) continue;

		stanje = 2;
		for(int i = 0; i<4; i++){
			if(tabla[i][i]!='O' && tabla[i][i]!='T') stanje = 0;
		}//O glavna dijagonala

		if (stanje == 2) {
			izlaz<<"Case #"<<counter+1<<": O won\n"; 
			continue;

		}


		stanje = 2;
		for(int i = 0; i<4; i++){
			if(tabla[i][3-i]!='O' && tabla[i][3-i]!='T') stanje = 0;
		}//O - sporedna dijagonala

		if (stanje == 2) {
			izlaz<<"Case #"<<counter+1<<": O won\n"; 
			continue;
		}


		for(int j = 0; j< 4; j++){
			stanje = 2;
			for(int i = 0; i<4; i++){
				if(tabla[j][i]!='O' && tabla[j][i]!='T') stanje = 0;
			}//O - vrste

			if (stanje == 2) {
				izlaz<<"Case #"<<counter+1<<": O won\n"; 
				break;
			}
			stanje = 2;
			for(int i = 0; i<4; i++){
				if(tabla[i][j]!='O' && tabla[i][j]!='T') stanje = 0;
			}//O - kolone

			if (stanje == 2) {
				izlaz<<"Case #"<<counter+1<<": O won\n"; 
				break;
			}
		}

		if(stanje == 2) continue;

		stanje = 3;
		for(int i = 0; i<4; i++)
			for(int j = 0; j<4; j++)
				if(tabla[i][j]=='.') stanje = 0;
		
		if (stanje == 3) {
			izlaz<<"Case #"<<counter+1<<": Draw\n"; 
			continue;
		}
		izlaz<<"Case #"<<counter+1<<": Game has not completed\n"; 
			
		
	}
}