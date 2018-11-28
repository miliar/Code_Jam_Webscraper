//============================================================================
// Name        : MagicTrick.cpp
// Author      : Rumman
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
	freopen(argv[1], "r", stdin);
	int temp;
	int t;
	cin >> t;
	for(int ti=0; ti<t; ti++) {
		// process each case here
		// ** get input
		int rowNo;
		int row1[4]; int row2[4];
		vector<int> common;

		cin >> rowNo;
		for(int i=0; i<4; i++) {
			if(i+1 != rowNo) {
				for(int j=0; j<4; j++) cin >> temp;
			}
			else {
				for(int j=0; j<4; j++) {
					cin >> row1[j];
				}
			}
		}

		cin >> rowNo;
		for(int i=0; i<4; i++) {
			if(i+1 != rowNo) {
				for(int j=0; j<4; j++) cin >> temp;
			}
			else {
				for(int j=0; j<4; j++) {
					cin >> row2[j];
				}
			}
		}

		// ** process rows
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				if(row1[i] == row2[j]) {
					common.push_back(row1[i]);
				}
			}
		}

		// ** display output
		cout << "Case #" << ti+1 << ": ";
		if(common.size() == 1)
			cout << common[0];
		else if(common.size() == 0)
			cout << "Volunteer cheated!";
		else
			cout << "Bad magician!";

		cout << endl;
	}
}
