	//
	//  Lawnmower.cpp
	//
	//
	//  Created by Alex Sorafumo on 13/04/13.
	//
	//

#include <iostream>

using namespace std;

int main(){
	int numCases, casesTested = 0;
	int lawnDims[101][2];
	bool able;
	int **lawn[101];
	bool **grassCutable[101];
	cin >> numCases;
		//Get inputs
	while (casesTested < numCases) {
		cin >> lawnDims[casesTested][1] >> lawnDims[casesTested][0];
		lawn[casesTested] = new int*[lawnDims[casesTested][1]];
		grassCutable[casesTested] = new bool*[lawnDims[casesTested][1]];
		for (int y = 0; y < lawnDims[casesTested][1]; y++) {
			lawn[casesTested][y] = new int[lawnDims[casesTested][0]];
			grassCutable[casesTested][y] = new bool[lawnDims[casesTested][0]];
			for (int x = 0; x < lawnDims[casesTested][0]; x++) {
				cin >> lawn[casesTested][y][x];
				grassCutable[casesTested][y][x] = false;
			}
		}
		casesTested++;
	}
	casesTested = 0;
	bool complete = true;
		//Process Inputs and Spit out output
	while (casesTested < numCases) {
		able = true;
		for (int length = 100; length > 0; length--) {
				//Enter from left side
			for (int y = 0; y < lawnDims[casesTested][1]; y++) {
				complete = true;
				for (int x = 0; x < lawnDims[casesTested][0]; x++) {
					if (lawn[casesTested][y][x] > length) {
						complete = false;
					}
				}
				if (complete) {
					for (int x = 0; x < lawnDims[casesTested][0]; x++) {
						if (lawn[casesTested][y][x] == length) {
							grassCutable[casesTested][y][x] = true;
						}
					}
				}
			}
				//Enter from right side
			for (int y = 0; y < lawnDims[casesTested][1]; y++) {
				complete = true;
				for (int x = lawnDims[casesTested][0] - 1; x >= 0; x--) {
					if (lawn[casesTested][y][x] > length) {
						complete = false;
					}
				}
				if (complete) {
					for (int x = 0; x < lawnDims[casesTested][0]; x++) {
						if (lawn[casesTested][y][x] == length) {
							grassCutable[casesTested][y][x] = true;
						}
					}
				}
			}
				//Enter from top
			for (int x = 0; x < lawnDims[casesTested][0]; x++) {
				complete = true;
				for (int y = 0; y < lawnDims[casesTested][1] ; y++) {
					if (lawn[casesTested][y][x] > length) {
						complete = false;
					}
				}
				if (complete) {
					for (int y = 0; y < lawnDims[casesTested][1]; y++) {
						if (lawn[casesTested][y][x] == length) {
							grassCutable[casesTested][y][x] = true;
						}
					}
				}
			}
				//Enter from bottom
			for (int x = 0; x < lawnDims[casesTested][0]; x++) {
				complete = true;
				for (int y = lawnDims[casesTested][1] - 1; y >= 0 ; y--) {
					if (lawn[casesTested][y][x] > length) {
						complete = false;
					}
				}
				if (complete) {
					for (int y = 0; y < lawnDims[casesTested][1]; y++) {
						if (lawn[casesTested][y][x] == length) {
							grassCutable[casesTested][y][x] = true;
						}
					}
				}
			}
		}
			//Check if all blocks where reachable
		for (int y = 0; y < lawnDims[casesTested][1]; y++) {
			for (int x = 0; x < lawnDims[casesTested][0]; x++) {
				if (!grassCutable[casesTested][y][x]){
					able = false;
					break;
				}
			}
			if (!able) {
				break;
			}
		}
#ifdef DEBUG
		for (int y = 0; y < lawnDims[casesTested][1]; y++) {
			for (int x = 0; x < lawnDims[casesTested][0]; x++){
				cout <<	lawn[casesTested][y][x] << ":" << grassCutable[casesTested][y][x] << " ";
			}
			cout << endl;
		}
#endif
		if (able)
			cout << "Case #" << casesTested + 1 << ": YES" << endl;
		else
			cout << "Case #" << casesTested + 1 << ": NO" << endl;
		casesTested++;
	}
	return 0;
}