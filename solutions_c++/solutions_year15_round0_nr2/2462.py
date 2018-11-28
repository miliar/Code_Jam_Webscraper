/*
 * pancakes.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: Jason
 */
#include <iostream>
#include <fstream>
using namespace std;


int main() {
	int c;
	ifstream cin;
	cin.open("input.txt");
	ofstream cout;
	cout.open("output.txt");
	cin >> c;
	for (int i = 1; i <= c; i++) {
		int t,min,max=0,s,d[1100];
		cin >> t;
		for (int j = 0; j < t; j++) {
			cin >> d[j];
			if (d[j]>max) max = d[j];
		}
		min = max;
		for (int j = 2; j < max; j++) {
			s=0;
			for (int k = 0; k < t; k++) s += (d[k]-1)/j;
			if (s+j<min) min = s+j;
		}
		cout << "Case #" << i << ": " << min << endl;
	}
}


