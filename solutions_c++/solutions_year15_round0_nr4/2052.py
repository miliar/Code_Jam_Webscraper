/*
 * omino.cc
 *
 *  Created on: Apr 11, 2015
 *      Author: maciek
 */

#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int main(int argc,char *argv[]){

	int N,X,R,L;
	int max, min;
	string s;
	ifstream fs(argv[1]);

	getline(fs, s);
	istringstream(s) >> N;
	for(int i = 0; i < N; i++){
		cout << "Case #" << i + 1 << ": ";
		getline(fs, s);
		istringstream(s) >> X >> R >> L;

		max = R>L ? R : L;
		min = R<L ? R : L;
		if (X > R*L) cout << "RICHARD" << endl;
		else if (R*L % X != 0) cout << "RICHARD" << endl;
		else if ( (int) ceil( X / 2.0) > min) cout << "RICHARD" << endl;
		else if ( X > max) cout << "RICHARD" << endl;
		else if (X == 4 && max == 4 && min == 2) cout << "RICHARD" << endl;
		else cout << "GABRIEL" << endl;


	}
}
