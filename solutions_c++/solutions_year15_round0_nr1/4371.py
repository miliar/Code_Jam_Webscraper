/*
 * ovation.cc
 *
 *  Created on: Apr 11, 2015
 *      Author: maciek
 */

#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

int main(int argc,char *argv[]){

	int N, maxS;
	string s, shn;
	ifstream fs(argv[1]);
	char c;
	vector<int> numP, totalP;
	int total,additional;

	getline(fs, s);
	istringstream(s) >> N;
	for(int i = 0; i < N; i++){

		cout << "Case #" << i+1 << ": ";
		getline(fs, s);
		istringstream(s) >> maxS;
		shn = s.substr(s.find(' ')+1, maxS+1);
		numP.clear();
		totalP.clear();
		total = additional = 0;
		for(int j = 0; j <= maxS; j++){
			numP.push_back(stoi(shn.substr(j,1)));
		}

		for(int j = 0; j <= maxS; j++){
			totalP.push_back(total);
			total += numP[j];
		}

		for(int j = 1; j <= maxS; j++){
			if(numP[j] > 0 && totalP[j] + additional < j) additional = j - totalP[j];
		}

		cout << additional << endl;
	}

}

