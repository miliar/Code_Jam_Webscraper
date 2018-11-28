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

const int maxn = 20;
long long D;
int S[maxn];
long long Result;

bool wayToSort(int i, int j) { return i > j; }
int solve() {
	// S pancakes on ith plate
	// D size of S
	int special = 0;
	//sort s 
	std::sort(S, S + D, wayToSort);
	int fmin = S[0];
	int min = S[0];
	int minNew = -1;
	bool nend = false;
	do {
		// if first to numbers are same dont end
		if (S[0] == S[1] && (special == 0 || nend)) {
			nend = true;
		}
		 else
		 {
			 nend = false;
		 }

		if (S[0] == 9 && special == 0&& (S[1] == 6 || S[1] == 3 || D ==1 || S[1]<3)) {
			int tmp = S[0];
			if (S[0] % 3 == 0) {
				S[0] = tmp / 3;
				S[D] = tmp / 3;
				S[D + 1] = tmp / 3;
			}
			else {
				if (S[0] % 3 == 1) {
					S[0] = tmp / 3 + 1;
					S[D] = tmp / 3;
					S[D + 1] = tmp / 3;
				}
				else {
					S[0] = tmp / 3 + 1;
					S[D] = tmp / 3 + 1;
					S[D + 1] = tmp / 3;
				}
			}
			D += 2;
			special += 2;
		}
		else {
			if (special != 0) {
				min = minNew;
			}
			int tmp = S[0];
			if (S[0] % 2 == 0) {
				S[0] = S[0] / 2;
			}
			else {
				S[0] = S[0] / 2 + 1;
			}
			S[D] = tmp / 2;
			D++;
			special++;
		}
		std::sort(S, S + D, wayToSort);
		minNew = special + S[0];
	} while (minNew <= min || nend);
	return std::min(min,fmin);
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
			myfile >> D;
			
			getline(myfile, line);

			// S nullen
			for (int i = 0; i < 15; i++) {
				S[i] = 0;
			}
			
			for (int k = 0; k < D; k++) {
				int as;
				myfile >> as;
				S[k] = as;
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

