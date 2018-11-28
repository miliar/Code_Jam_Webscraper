#include <iostream>
#include <cstdio>
#include <string>
#include <fstream>
#include <sstream>
#include <cmath>
#include <stdlib.h>
using namespace std;
bool isdecimal(double);
bool isinverso(long);

int main(int argc, char *argv[]) {
	long n, ni, nf, ns;
	double d;
	int cont=0, i=0, j=0, pos, tam;
	string lni, lnf, filenamein, filenameout, linea, archivo;

	filenamein = "C-small-attempt0.in";
	filenameout = "C-small-attempt0.out";
	ifstream filein (filenamein.c_str());
	ofstream fileout (filenameout.c_str());
	
	getline(filein, linea);
	stringstream str(linea);
	str >> n;
	n++;
	int x = 1;
	while (x < n){
		getline(filein, linea);
		tam = linea.size();
		pos = linea.find(' ');
		lni = linea.substr(0, pos);
		lnf = linea.substr(pos+1, tam);
		stringstream str1(lni);
		str1 >> ni;
		stringstream str2(lnf);
		str2 >> nf;
		
		for(j = nf; j >= ni; j--){
			d = (double) sqrt(j);
				if (!isdecimal(d)){
					ns = (long) d;
					if(isinverso(ns) and isinverso(j)){
						cont++;
					}
				}
			}
		
		fileout << "Case #" << x << ": " << cont << endl;
		cont = 0;
		x++;
	}
	return 0;
}

bool isdecimal(double num) 
{ 
	long n_entero = (long) num; 
	if(num != n_entero) 
		return 1; 
	else 
		return 0; 
}

bool isinverso(long numero){
	long residuo, inverso=0;
	residuo = numero;
	while(residuo>0){
		inverso = (inverso * 10) + (residuo % 10);
		residuo /= 10;
	}
	if(numero==inverso)
		return 1;
	else 
		return 0;
}
