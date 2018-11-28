#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <fstream>
#include <list>
// stringstreams
#include <sstream>
using namespace std;

#define M_PI 3.14159265358979323846

const int maxn = 100 + 5;
const int maxw = 999999;
long long X, R, C;
int S[maxn];
string Result;
int erg[maxn][maxw];
int d[maxw]; // durchschnitt von erg


bool solve() {
	// returns true when gabriel wins
	// X size dominion
	// R * C field to fill
	// 442, 422 is richi
	if ((X == 4 && R*C == 8) || (X == 4 && R*C == 4))  {
		return false;
	}
	if (X == 3 && R*C == 3) {
		return false;
	}
	
	if (X == 1) {
		return true;
	}
	
	// teilbarkeit
	if ((R*C) % X != 0) { return false; }

	if (X > R*C) { return false; }

	return true;
}


int main(int argc, char* argv[])
{
	//input variables
	int numberOfTestCases;

	ifstream myfile;
	ofstream outputFile;
	string line;
	myfile.open("input.in");
	outputFile.open("output.out");

	if (myfile.is_open()){
		myfile >> numberOfTestCases;
		getline(myfile, line);

		for (int q = 0; q < numberOfTestCases; q++){
			cout << q << "\n";

			// input
			myfile >> X;
			
			myfile >> R;
			myfile >> C;

			//solve problem			
			if (solve()) {
				Result = "GABRIEL";
			} else {
				Result = "RICHARD";
			}
					

			//output			
			outputFile << "Case #" << q+ 1 << ": " << Result;
			

			if (q + 1 != numberOfTestCases)
				outputFile << "\n";
		};
		myfile.close();
		outputFile.close();
	}
	else {
		cout << "unable to open file";
	}
	string name;

	cin >> name;
	return 0;
}

