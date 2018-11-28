#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int product[5][5] = {{0, 0,  0,  0,  0},
					 {0, 1,  2,  3,  4},
					 {0, 2, -1,  4, -3},
					 {0, 3, -4, -1,  2},
					 {0, 4,  3, -2, -1}};

int main() {
	int numCases;
	cin >> numCases;
	
	for(int x = 1; x <= numCases; x++) {
		int repSize;
		int numReps;
		cin >> repSize >> numReps;
		int totalLength = repSize * numReps;
		
		string rep;
		cin >> rep;
		
		int temp = rep[0] - 'g';
		bool neg = false;
		for(int r = 1; r < repSize; r++) {
			temp = product[temp][rep[r] - 'g'];
			if(temp < 0) {
				temp *= -1;
				neg = !neg;
			}
		}
		int repVal = temp;
		bool repNeg = neg;
		
		int totalVal = repVal;
		neg = false;
		for(int r = 1; r < numReps; r++) {
			totalVal = product[totalVal][repVal];
			if(totalVal < 0) {
				neg = !neg;
				totalVal *= -1;
			}
		}
		if(repNeg && (numReps % 2) == 1) {
			neg = !neg;
		}
		bool totalNeg = neg;
		
		if(totalVal != 1 || !totalNeg) {//final result does not match -1 = i*j*k
			cout << "Case #" << x << ": NO\n";
			continue;
		} else if(totalLength < 3) {//too few letters
			cout << "Case #" << x << ": NO\n";
			continue;
		}
		
		int neededForI = 0;
		if(rep[0] == 'i') {
			neededForI = 1;
		} else {
			temp = rep[0] - 'g';
			neg = false;
			for(int r = 1; r < totalLength && r < 4 * repSize; r++) {
				temp = product[temp][rep[r % repSize] - 'g'];
				if(temp < 0) {
					temp *= -1;
					neg = !neg;
				}
				if(!neg && temp == 2) {
					neededForI = r;
					break;
				}
			}
		}
		
		if(!neededForI) {
			cout << "Case #" << x << ": NO\n";
			continue;
		}
		
		int neededForK = 0;
		if(rep[repSize - 1] == 'k') {
			neededForK = 1;
		} else {
			temp = rep[repSize - 1] - 'g';
			neg = false;
			for(int r = totalLength - 2; r >= 0 && r > totalLength - (1 + (4 * repSize)); r--) {
				temp = product[rep[r % repSize] - 'g'][temp];
				if(temp < 0) {
					temp *= -1;
					neg = !neg;
				}
				if(!neg && temp == 4) {
					neededForK = totalLength - r;
					break;
				}
			}
		}
		
		if(!neededForK) {
			cout << "Case #" << x << ": NO\n";
			continue;
		}
		
		if(neededForI + neededForK >= totalLength) {
			cout << "Case #" << x << ": NO\n";
			continue;
		}
		
		cout << "Case #" << x << ": YES\n";
	}
}
