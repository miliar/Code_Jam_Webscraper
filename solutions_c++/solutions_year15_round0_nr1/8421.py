/*
///		Develop by NRG		///
*/

#include <vector>
#include <iostream>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <fstream>
#include <cstdio>

#define ll long long

#define min(x, y) ((x) < (y) ? (x) : (y))

using namespace std;

int main(){
	vector <int> shyness(1001, 0);
	int test = 0, sMax = 0, answer = 0, curCnt = 0, delta = 0;
	cin >> test;
	for (int iTest = 1; iTest <= test; iTest++) {
		cin >> sMax;
		cin.get();
		answer = curCnt = 0;
		for (int iShyness = 0; iShyness <= sMax; iShyness++) {
			shyness[iShyness] = cin.get() - '0';
		}
		for (int iShyness = 0; iShyness <= sMax; iShyness++) {
			if (0 == shyness[iShyness]) {
				continue;
			}
			if (curCnt < iShyness) {
				delta = iShyness - curCnt;
				curCnt += delta + shyness[iShyness];
				answer += delta;
			}
			else {
				curCnt += shyness[iShyness];
			}
		}
		cout << "Case #" << iTest << ": " << answer << endl;
	}
	return 0;
}
