//============================================================================
// Name        : codejam14qualA.cpp
// Author      : Kishore Rajasekar
// Version     :
// Copyright   : //Copyright 2013 - Kishore Rajasekar - kishore@cise.ufl.edu
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <fstream>
#include <iostream>
using namespace std;

int main() {
	ofstream outf("qualA.out");
	ifstream inf("qualA.in");
	if (!outf || !inf){
		cout << "error opening files" <<endl;
		return 1;
	}

	int n, t, value, hits;
	int r1[4], r2[4];
	inf >> n;

	for(int i =0; i<n; i++){
		int r1n;
		inf >> r1n;
		//cout << r1n <<endl;
		int skip = 4*(r1n-1);
		while (skip>0){
			--skip;
			inf >> t;
		}
		inf >> r1[0];
		inf >> r1[1];
		inf >> r1[2];
		inf >> r1[3];
		//cout << r1[0] << r1[1] << r1[2] << r1[3] <<endl;
		skip = 4*(4-r1n);
		while (skip>0){
			--skip;
			inf >> t;
		}
		int r2n;
		inf >> r2n;
		//cout << r2n <<endl;
		skip = 4*(r2n-1);
		while (skip>0){
			--skip;
			inf >> t;
		}
		inf >> r2[0];
		inf >> r2[1];
		inf >> r2[2];
		inf >> r2[3];
		//cout << r2[0] << r2[1] << r2[2] << r2[3] <<endl;
		skip = 4*(4-r2n);
		while (skip>0){
			--skip;
			inf >> t;
		}
		hits = 0;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				if (r1[j] == r2[k]){
					hits++;
					value = r1[j];
				}
			}
		}
		switch (hits){
		case 0:
			outf << "Case #"<<i+1<<": Volunteer cheated!"<<endl;break;
		case 1:
			outf << "Case #"<<i+1<<": "<<value<<endl;break;
		default:
			outf << "Case #"<<i+1<<": Bad magician!"<<endl;break;
		}
	}

	return 0;
}
