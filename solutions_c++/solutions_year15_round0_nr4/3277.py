// ProblemD.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <iostream>

using namespace std;

int main(void) {
	int testcases, X, R, C;
	freopen("D-small-attempt3.in", "r", stdin);
	freopen("output.out", "w", stdout);
	cin >> testcases;

	for (int i = 1; i <= testcases; i++) {
		cin >> X >> R >> C;
		if (X == 1){ 
			cout << "Case #" << i << ": " << "GABRIEL" << endl;
		}
		else if (X > R*C){
			cout << "Case #" << i << ": " << "RICHARD" << endl;
		}
		else if (X == 2){
			if (R*C % 2 == 0){
				cout << "Case #" << i << ": " << "GABRIEL" << endl;
			}
			else {
				cout << "Case #" << i << ": " << "RICHARD" << endl;
			}
		}
		else if (X == 3){
			if (R*C == 6 || R*C == 9 || R*C == 12){
				cout << "Case #" << i << ": " << "GABRIEL" << endl;
			}
			else { 
				cout << "Case #" << i << ": " << "RICHARD" << endl;
			}
		}
		else {
			if (R*C == 12 || R*C == 16){
				cout << "Case #" << i << ": " << "GABRIEL" << endl;
			}
			else {
				cout << "Case #" << i << ": " << "RICHARD" << endl;
			}
		}

	

	}
	return 0;
}
