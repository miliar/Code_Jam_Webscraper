// ProblemA.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int main(void) {
	int testcases, sMax, friendsNeeded;
	string sAudience;
	int* A;
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int sum = 0;
	cin >> testcases;

	for (int i = 1; i <= testcases; i++) { 
		friendsNeeded = 0;
		cin >> sMax >> sAudience;
		A = new int[sMax+1];
		
		for (int j = sMax ; j >= 0; j--) {
			int iAudience = sAudience.c_str()[j] - '0';
			A[j] = iAudience;			
		}
		sum = 0;
		for (int k = 0; k <= sMax; k++) {
			if (sum > k){
				sum += A[k];
				continue;
			}
			while (k>sum) {
				friendsNeeded++;
				sum++;
			}
			sum += A[k];

		}


		cout << "Case #" << i << ": " << friendsNeeded << endl;
	}
	return 0;
}