using namespace std;
#include <iostream>
#include <fstream>
#include <math.h>
#include <string>

int main(){
	int ncasos, cont;
	bool menos = true;
	string N;
	fstream infile("prueba.in");
	ofstream outfile("solu.out");
	infile >> ncasos;
	for (int i = 0; i < ncasos; i++)
	{
		infile >> N;
		cont = 0;
		menos = true;
		while (menos){
				int k = 0;
				menos = false;
				while (k <= N.length()){
					if (N[k] == '-') menos = true;
					k++;
				}
				if (menos){
				//se busca desde arriba el maximo numero de + seguidos
				int cuentaUp = 0;
				while (N[cuentaUp] == '+' && cuentaUp < N.length())	cuentaUp++;
				if (cuentaUp > 0){
					cont++;
					//se les da la vuelta 
					for (int l = 0; l < cuentaUp; l++)	N[l] = '-';					
				}
				//se busca el primer - desde abajo
				int cuentaDown = N.length() - 1;
				while (N[cuentaDown] == '+')cuentaDown--;
				if (cuentaDown >= 0) cont++;
				//voltear
				//primero copiamos en un array aparte
				string aux;
				for (int m = cuentaDown; m >= 0; m--) aux += N[m];
				int n = 0;
					for (int m = 0; m <= cuentaDown; m++){
						if (aux[m] == '-')	N[n] = '+'; 
						if (aux[m] == '+')	N[n] = '-';
						n++;
					}
				}
		}
		outfile << "Case #" << i+1 << ": "<< cont << endl;
	}
	return 0;
}