#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int counter = 0;

// string magicSmall(int first, int second, int m1[4][4], int m2[4][4], int m, int n) {
//string magicSmall(int first, int second, int (*m1)[], int (*m2)[], int m, int n) {
string magicSmall(int first, int second, int m1[4][4], int m2[4][4]) {	
	string decision;
	
	int same = 0;
	int total = 0;
	
	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++)
			if (m1[first-1][i] == m2[second-1][j]) {
				same = m1[first-1][i];
				total += 1;
			}

	if (total == 1) {
		if (same/10==1) decision.push_back('1');
		decision.push_back(same % 10 + '0');
		//decision = same + "0"; //????????????? int to string
	} else if (total < 1)
		decision = "Volunteer cheated!";		
	else
		decision = "Bad magician!";

	
	return decision;
}
	// Case #1: 7
	// Case #2: Bad magician!
	// Case #3: Volunteer cheated!


void process() {
	// string decision = "Good";
	// cout << "Case #" << counter++ << ": " << decision << endl;



	int first, second;
	int m1[4][4], m2[4][4];
	
	
	cin >> first;
	
	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++)
			cin >> m1[i][j];

	cin >> second;

	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++)
			cin >> m2[i][j];

	
	// cout << " first- " << first << " second- " << second << endl;

	//string decision = "Good";
	//string result = magicSmall(first, second, m1, m2, 4, 4);
	string result = magicSmall(first, second, m1, m2);
	cout << "Case #" << ++counter << ": " << result << endl;
	
	//cout << endl;
	return;
}


int main() {
	int t, k;
	scanf("%d", &t); // read the number of cases
	//cin >> t >> k; // cout << t << endl; // cout << k << endl;
	
	while (t--) {
		process();
	}

	return 0;
}