//============================================================================
// Name        : codejam14qualB.cpp
// Author      : Kishore Rajasekar
// Version     :
// Copyright   : //Copyright 2013 - Kishore Rajasekar - kishore@cise.ufl.edu
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <fstream>
#include <iostream>
#include <iomanip>
#define MUL 100000
using namespace std;

int main() {
	ofstream outf("qualB.out");
	ifstream inf("qualB.in");
	if (!outf || !inf){
		cout << "error opening files" <<endl;
		return 1;
	}
	cout << "Hello Universe!" << endl; // prints Hello Universe!
	long int n, p;
	long double c,f,x;
	long double current, temp;
	inf >> n;
	for(int i =0; i<n; i++){
		inf >> c >> f >> x;
		current = -1;
		temp =0; p =1;
		do{
			if (current == -1.0) current = MUL*x / 2;
			else current = temp;
			temp = MUL*(x / (2+p*f));
			for(int j = 0; j<p; j++){
				temp += MUL*(c / (2+j*f));
			}
			++p;
		}while (temp < current);
		current /= MUL;
		outf << "Case #"<<i+1<<": "<< std::fixed << std::setprecision( 20 )
         << current << endl;
	}
	return 0;
}
