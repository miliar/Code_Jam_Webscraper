#include <iostream>
#include <fstream>
using namespace std;

fstream in ("/home/m/Google Code JAM/test.txt");
int dim, x, y, z;
char tmp, Z='?';

int main(){
	in>>dim;
	char m[4][4][dim];
	char win[dim];
	for(z=0; z<dim; z++){
		for(y=0; y<4; y++){
			for(x=0; x<4 and in>>tmp; x++){
				m[y][x][z]=tmp;
			}
		}

		for(int v=0; v<2; v++){
            if(v==0) Z='X';
			if(v==1) Z='O';
			for(int i=0; i<4; i++){
				if(	(m[i][0][z]==Z or m[i][0][z]=='T') and
					(m[i][1][z]==Z or m[i][1][z]=='T') and
					(m[i][2][z]==Z or m[i][2][z]=='T') and
					(m[i][3][z]==Z or m[i][3][z]=='T')){win[z]=Z; break;}
			}

			for(int i=0; i<4; i++){
				if(	(m[0][i][z]==Z or m[0][i][z]=='T') and
					(m[1][i][z]==Z or m[1][i][z]=='T') and
					(m[2][i][z]==Z or m[2][i][z]=='T') and
					(m[3][i][z]==Z or m[3][i][z]=='T')){win[z]=Z; break;}
			}
			if(	(m[0][0][z]==Z or m[0][0][z]=='T') and
				(m[1][1][z]==Z or m[1][1][z]=='T') and
				(m[2][2][z]==Z or m[2][2][z]=='T') and
				(m[3][3][z]==Z or m[3][3][z]=='T')){win[z]=Z; break;}

			if(	(m[0][3][z]==Z or m[0][3][z]=='T') and
				(m[1][2][z]==Z or m[1][2][z]=='T') and
				(m[2][1][z]==Z or m[2][1][z]=='T') and
				(m[3][0][z]==Z or m[3][0][z]=='T')){win[z]=Z; break;}

			if(win[z]!='X' and win[z]!='O'){
				for(int s=0; s<4; s++){
					for(int i=0; i<4; i++){
						if(m[s][i][z]=='.') {win[z]='N'; break;}
					}
				}
				if(win[z]!='N') win[z]='D';
			}
		}
	}
	for(int i=0; i<dim; i++){
		switch(win[i]){
			case 'X': {cout << "Case #" << i+1 << ": X won" << endl; break;}
			case 'O': {cout << "Case #" << i+1 << ": O won" << endl; break;}
			case 'D': {cout << "Case #" << i+1 << ": Draw" << endl; break;}
			case 'N': {cout << "Case #" << i+1 << ": Game has not completed" << endl; break;}
		}
	}
	return 0;
}