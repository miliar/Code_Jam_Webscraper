//============================================================================
// Name        : Bullseye.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

typedef unsigned int tipo;

int main() {
	ifstream fin("C:\\Users\\Daniel\\Downloads\\Firefox\\A-small-attempt0.in");
	ofstream fout("C:\\Users\\Daniel\\Downloads\\Firefox\\A-small-attempt0.out");
	unsigned int T;
	fin >> T;

	for (unsigned int k=1; k<=T; k++) {
		tipo r, t, acum = 0, aux = 0, cont=0, n=1;
		fin >> r >> t;
		aux = (pow(r+n, 2))-pow(r+n-1, 2);
		while (acum + aux <= t) {
			acum += aux;
			cont++;
			n+=2;
			aux = (pow(r+n, 2))-pow(r+n-1, 2);
		}
		fout << "Case #" << k << ": " << cont << endl;
	}

	return 0;
}
