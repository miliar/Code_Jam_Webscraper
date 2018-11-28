// A.cpp: define el punto de entrada de la aplicación de consola.
//

#include "stdafx.h"
#include "stdafx.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
using namespace std;

#define lld unsigned long long int

string solve(int N){
	if(N==0) return "INSOMNIA";

	int counter = 1;
	int vv[10] = { 0,0,0,0,0,0,0,0,0,0};
	
	lld _N = N;
	while(true){
	std::string _number = std::to_string(_N);
	
	for(int i=0; i<_number.size(); i++){
		int index = (int)_number.at(i)-48;
		vv[index] = 1;
	}

	//Salida si todos los numeros se han visto
	int out = 1;
	for(int i=0; i<10; i++){
		if(vv[i]==0) out = 0;
	}

	if(out==1) break;

	//Si no se salio, duplicar
	_N = N * ++counter;
	}

	return std::to_string(_N);
}


int main() {
	//Open the file
	std::ifstream infile;
	infile.open ("A-large.in");
	std::ofstream  outfile;
	outfile.open ("A-large.out");

	//Read the number of cases
	int T, N, count = 0;
	infile >> T;

	while(T-->0){
		infile >> N;
		std::string value = solve(N);
		outfile << "Case #" << ++count << ": " << value.c_str()  << (T>0?"\n":"");
	}

	return 0;
}

