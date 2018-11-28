#include <iostream>
#include <cstdio>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;
int main(int argc, char *argv[]) {
	int n, i, x;
	string f1, f2, f3, f4, filenamein, filenameout, linea, archivo;
	bool owon, xwon, punto;
	string::size_type sz;
	
	owon = xwon = punto = false;
	
	filenamein = "A-large.in";
	filenameout = "A-large.out";
	ifstream filein (filenamein.c_str());
	ofstream fileout (filenameout.c_str());
	
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	getline(filein, linea);
	stringstream str(linea);
	str >> n;
	//cin >> n;
	//scanf("%d",&n);
	n++;
	for(i = 1; i < n; i++){
		//cin >> f1 >> f2 >> f3 >> f4;
		getline(filein,f1);
		getline(filein,f2);
		getline(filein,f3);
		getline(filein,f4);
		//Casos de Ganado
		// FILAS O
		if((f1[0]=='O' or f1[0]=='T') and 
		(f1[1]=='O' or f1[1]=='T') and 
		(f1[2]=='O' or f1[2]=='T') and 
		(f1[3]=='O' or f1[3]=='T'))
			owon = true;
		else if((f2[0]=='O' or f2[0]=='T') and 
		(f2[1]=='O' or f2[1]=='T') and 
		(f2[2]=='O' or f2[2]=='T') and 
		(f2[3]=='O' or f2[3]=='T'))
			owon = true;
		else if((f3[0]=='O' or f3[0]=='T') and 
		(f3[1]=='O' or f3[1]=='T') and 
		(f3[2]=='O' or f3[2]=='T') and 
		(f3[3]=='O' or f3[3]=='T'))
			owon = true;
		else if((f4[0]=='O' or f4[0]=='T') and 
		(f4[1]=='O' or f4[1]=='T') and 
		(f4[2]=='O' or f4[2]=='T') and 
		(f4[3]=='O' or f4[3]=='T'))
			owon = true;
		// FILAS X
		else if((f1[0]=='X' or f1[0]=='T') and 
		(f1[1]=='X' or f1[1]=='T') and 
		(f1[2]=='X' or f1[2]=='T') and 
		(f1[3]=='X' or f1[3]=='T'))
			xwon = true;
		else if((f2[0]=='X' or f2[0]=='T') and 
		(f2[1]=='X' or f2[1]=='T') and 
		(f2[2]=='X' or f2[2]=='T') and 
		(f2[3]=='X' or f2[3]=='T'))
			xwon = true;
		else if((f3[0]=='X' or f3[0]=='T') and 
		(f3[1]=='X' or f3[1]=='T') and 
		(f3[2]=='X' or f3[2]=='T') and 
		(f3[3]=='X' or f3[3]=='T'))
			xwon = true;
		else if((f4[0]=='X' or f4[0]=='T') and 
		(f4[1]=='X' or f4[1]=='T') and 
		(f4[2]=='X' or f4[2]=='T') and 
		(f4[3]=='X' or f4[3]=='T'))
			xwon = true;
		//COLUMNAS O
		else if((f1[0]=='O' or f1[0]=='T') and 
			(f2[0]=='O' or f2[0]=='T') and 
			(f3[0]=='O' or f3[0]=='T') and 
			(f4[0]=='O' or f4[0]=='T'))
				owon = true;
		else if((f1[1]=='O' or f1[1]=='T') and 
			(f2[1]=='O' or f2[1]=='T') and 
			(f3[1]=='O' or f3[1]=='T') and 
			(f4[1]=='O' or f4[1]=='T'))
				owon = true;
		else if((f1[2]=='O' or f1[2]=='T') and 
			(f2[2]=='O' or f2[2]=='T') and 
			(f3[2]=='O' or f3[2]=='T') and 
			(f4[2]=='O' or f4[2]=='T'))
				owon = true;
		else if((f1[3]=='O' or f1[3]=='T') and 
			(f2[3]=='O' or f2[3]=='T') and 
			(f3[3]=='O' or f3[3]=='T') and 
			(f4[3]=='O' or f4[3]=='T'))
				owon = true;
		//COLUMNAS X
		else if((f1[0]=='X' or f1[0]=='T') and 
			(f2[0]=='X' or f2[0]=='T') and 
			(f3[0]=='X' or f3[0]=='T') and 
			(f4[0]=='X' or f4[0]=='T'))
				xwon = true;
		else if((f1[1]=='X' or f1[1]=='T') and 
			(f2[1]=='X' or f2[1]=='T') and 
			(f3[1]=='X' or f3[1]=='T') and 
			(f4[1]=='X' or f4[1]=='T'))
				xwon = true;
		else if((f1[2]=='X' or f1[2]=='T') and 
			(f2[2]=='X' or f2[2]=='T') and 
			(f3[2]=='X' or f3[2]=='T') and 
			(f4[2]=='X' or f4[2]=='T'))
				xwon = true;
		else if((f1[3]=='X' or f1[3]=='T') and 
			(f2[3]=='X' or f2[3]=='T') and 
			(f3[3]=='X' or f3[3]=='T') and 
			(f4[3]=='X' or f4[3]=='T'))
				xwon = true;
		//DIAGONALES O
		else if((f1[0]=='O' or f1[0]=='T') and 
			(f2[1]=='O' or f2[1]=='T') and 
			(f3[2]=='O' or f3[2]=='T') and 
			(f4[3]=='O' or f4[3]=='T'))
				owon = true;
		else if((f1[3]=='O' or f1[3]=='T') and 
			(f2[2]=='O' or f2[2]=='T') and 
			(f3[1]=='O' or f3[1]=='T') and 
			(f4[0]=='O' or f4[0]=='T'))
				owon = true;
		//DIAGONALES X
		else if((f1[0]=='X' or f1[0]=='T') and 
			(f2[1]=='X' or f2[1]=='T') and 
			(f3[2]=='X' or f3[2]=='T') and 
			(f4[3]=='X' or f4[3]=='T'))
				xwon = true;
		else if((f1[3]=='X' or f1[3]=='T') and 
			(f2[2]=='X' or f2[2]=='T') and 
			(f3[1]=='X' or f3[1]=='T') and 
			(f4[0]=='X' or f4[0]=='T'))
				xwon = true;
		
		//Termino?
		if (!owon and !xwon){
			for(x = 0;x < 4; x++){
				if(f1[x] == '.'){
					punto = true;
					break;
				}
				if(f2[x] == '.'){
					punto = true;
					break;
				}
				if(f3[x] == '.'){
					punto = true;
					break;
				}
				if(f4[x] == '.'){
					punto = true;
					break;
				}
			}
		}
		
		//Resultados
		if(owon)
			fileout << "Case #" << i << ": " << "O won" << endl;
		else if(xwon)
			fileout << "Case #" << i << ": " << "X won" << endl;
		else if(punto)
			fileout << "Case #" << i << ": " << "Game has not completed" << endl;
		else
			fileout << "Case #" << i << ": " << "Draw" << endl;
		owon = xwon = punto = false;
		getline(filein, linea);
	}
}
