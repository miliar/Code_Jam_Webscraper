#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <ctime>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <cctype>
#include <cstdlib>
using namespace std;



int main(){
	ifstream ent; ofstream sal; ent.open("entrada.txt"); sal.open("salida.out");
	int numcasos; string S = ""; ent >> numcasos; int cont[10];
	for (int k = 1; k <= numcasos;++k){
		sal << "Case #" << k << ": ";
		ent >> S; int contz = 0, contx = 0, contu = 0, contg = 0,contw=0,cont1,cont3,cont5,cont9,cont7;
		for (int i = 0; i < S.size(); ++i){
			if (S[i] == 'Z')++contz;
			else if (S[i] == 'W')++contw;
			else if (S[i] == 'X')++contx;
			else if (S[i] == 'U')++contu;
			else if (S[i] == 'G')++contg;
		}
		cont[0] = contz; cont[2] = contw; cont[6] = contx; cont[8] = contg; cont[4] = contu;
		int coo = contz + contw + contu, coh = contg, cof = contu, conto = 0, conth = 0, contf = 0, conts = 0, cos = contx;
		for (int i = 0; i<S.size(); ++i){
			if (S[i] == 'O')++conto;
			else if (S[i] == 'H')++conth;
			else if (S[i] == 'F')++contf;
			else if (S[i] == 'S')++conts;
		}
		cont[1] = conto - coo; cont[3] = conth - coh; cont[5] = contf - cof; cont[7] = conts - cos;
		int conti = 0, coi = contg + contx + cont[5];
		for (int i = 0; i<S.size(); ++i){
			if (S[i] == 'I')++conti;
		}
		cont[9] = conti - coi;
		for (int i = 0; i < 10; ++i){
			for (int j = 0; j < cont[i]; ++j){
				sal << i;
			}
		}
		sal << '\n';
	}
	ent.close(); sal.close();
	return 0;
}