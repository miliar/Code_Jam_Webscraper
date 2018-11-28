/*
 * shroom.cpp
 *
 *  Created on: Apr 17, 2015
 *      Author: Jason
 */

#include <iostream>
#include <fstream>
using namespace std;

int a[11000];
int main() {
	ifstream cin;
	cin.open("input.txt");
	ofstream cout;
	cout.open("output.txt");

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int n, d=0, y=0, z=0;
		cin >> n;
		for (int j = 0; j < n; j++) {
			cin >> a[j];
			if (j > 0 && (a[j] < a[j-1]) && (d < a[j-1]-a[j])) d=a[j-1]-a[j];
		}
		for (int j = 0; j < n-1; j++) {
			if (a[j+1]<a[j]) {
				y+=a[j]-a[j+1];
				z+=min(d,a[j]);
			} else {
				z+=min(d,a[j]);
			}
		}
		cout << "Case #" << i << ": " << y << " " << z << endl;
	}
	return 0;
}
