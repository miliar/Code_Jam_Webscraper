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

struct todo{
	char letra = ' ';
	int cantidad = 0;
};

bool operator<( todo dat , todo dato){
	return dat.cantidad>dato.cantidad;
}

bool operator>(todo dat, todo dato){
	return dat.cantidad<dato.cantidad;
}

bool operator==(todo dat, todo dato){
	return dat.cantidad==dato.cantidad;
}



int main(){
	ifstream ent; ofstream sal; ent.open("entrada.txt"); sal.open("salida.out");
	int numcasos;
	ent >> numcasos;
	for (int y = 1; y <= numcasos; ++y){
		sal << "Case #" << y << ": "; vector<todo> esto(26);
		esto[0].letra = 'A';
		for (int i = 1; i < 26; ++i)esto[i].letra = esto[i - 1].letra+1;
		int letras, total = 0; ent >> letras;
		for (int i = 0; i < letras; ++i){
			ent >> esto[i].cantidad;
			total += esto[i].cantidad;
		}string sali = "";
		while (total > 0){
			sort(esto.begin(), esto.end());
			sali.push_back(esto[0].letra); --total; --esto[0].cantidad;
			float mitad = float(total) / 2;
			if (total != 0 && esto[0].cantidad>mitad){
				sali.push_back(esto[0].letra); --total;
				--esto[0].cantidad;
			}
			else if (total != 0 && esto[1].cantidad>mitad){
				sali.push_back(esto[1].letra); --total;
				--esto[1].cantidad;
			}
			sal << sali; sali = "";
			if (total != 0)sal << ' ';
		}
		sal << '\n';
	}
	ent.close(); sal.close();
	return 0;
}