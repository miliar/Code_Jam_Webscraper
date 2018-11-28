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
long long N;
int S[maxn];
long long Result;
int erg[maxn][maxw];
int d[maxw]; // durchschnitt von erg


int solve() {
	// S shyness level S[1] = 4, 4 persons with shyness 1
	// N size of S
	long long sum = 0;
	int n = 0;
	for (int i = 0; i <= N; i++) {
		// sondernfall beginn
		if ((i == 0 && S[0] == 0) || (sum < i)) {			
			n++;
			sum ++;
		}
		sum += S[i];
	}
	return n;
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
			myfile >> N;

			myfile >> line;
			int k = 0;
			for (char& c : line) {
				S[k] = c - '0';
				k++;
			}

			//solve problem			
			Result = solve();

			

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

