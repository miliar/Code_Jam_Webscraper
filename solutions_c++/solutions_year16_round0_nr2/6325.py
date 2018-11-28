// B.cpp: define el punto de entrada de la aplicación de consola.
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


int solve(string P){
	//Create a dinamic array
	int* vv = new int[P.size()];
	int* vt = new int[P.size()];
	//Populate the array
	for(int i=0; i<P.size();i++)
		vv[i] = P.at(i)=='+'? 1:0;

	if(P.size()==1 && vv[0]==1) return 0;
	if(P.size()==1 && vv[0]==0) return 1;

	int flips = 0;
	while(true){
		//Create exit condition
		int out = 1;
		for(int i=0; i<P.size();i++)
			if(vv[i]==0) out = 0;
		if(out==1) break;

		//Get the index to flip
		int first = vv[0];
		int last = P.size();
		for(int i=0; i<P.size();i++){
			int value = vv[i];
			if(value!=first){
				last = i;
				break;
			}
		}

		//Flip it!!!
		for(int i=0; i<last; i++){
			vt[i] = vv[last-i-1];
		}
		//Reverse it!!
		for(int i=0; i<last; i++){
			vv[i] = vt[i]==0?1:0;
		}

		flips++;
	}

	return flips;
}


int main() {
	//Open the file
	std::ifstream infile;
	infile.open ("B-large.in");
	std::ofstream  outfile;
	outfile.open ("B-large.out");

	//Read the number of cases
	int T, N, count = 0;
	infile >> T;

	while(T-->0){
		string pancake;
		infile >> pancake;
		int N = solve(pancake);
		outfile << "Case #" << ++count << ": " << N << (T>0?"\n":"");
	}

	return 0;
}


