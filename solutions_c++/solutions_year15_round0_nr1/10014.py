#include <iostream>
#include <stdio.h>
#include <math.h>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

ifstream inFile("ovation.txt");
ofstream outFile("ovationResults.txt");

int getDifference(vector<int> &values, int size) {
	int totalStanding = 0;
	int totalPeople = 0;
	for (int m = 0; m < size; m++) {
		if (m == 0) {
			totalStanding += values[0];
			totalPeople += values[0];
		}
		else {
			if (totalStanding >= m) {
				totalStanding += values[m];
			}
			totalPeople += values[m];
		}
		// printf("\n %d", values[m]);
	}
	return totalPeople - totalStanding;
}

void solveCase(int cNo) {
	int minFriends = 0;
	int n;
	inFile >> n;
	int x;
	inFile >> x;
	vector<int> values(n+1);
	for (int m = n; m >= 0; m--) {
		values[m] = x % 10;
		x /= 10;
	}
	// read the stupid input file here

	while (getDifference(values, n + 1) > 0) {
		values[0]++;
		minFriends++;
	}
	outFile << "Case #";
	outFile << cNo;
	outFile << ": ";
	outFile << minFriends;
	outFile << "\n";
	printf("\n Case #%d: %d", cNo, minFriends);
}

void main() {
	int x;
	inFile >> x;
	for (int i = 0; i < x; i++) {
		solveCase(i+1);
	}
	inFile.close();
}