// A.cpp: define el punto de entrada de la aplicación de consola.
//

#include "stdafx.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
using namespace std;

int main() {
	//Open the file
	std::ifstream infile;
	infile.open ("A-large.in");
	std::ofstream  outfile;
	outfile.open ("A-large.out");

	//Read the number of cases
	int T, count = 1;
	infile >> T;

	while(T-->0){
		std::string S, W;
		infile >> S;

		for(int i=0; i < S.size(); i++){
			if(W.size() == 0) W = S.at(0);
			else{
				if(S.at(i) >= W.at(0)) 
					W = S.at(i) + W; 
				else
					W = W + S.at(i); 
			}
		}

		outfile << "Case #" << count++ << ": " << W << (T>0?"\n":""); 

	}

	return 0;
}

