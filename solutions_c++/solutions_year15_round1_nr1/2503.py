// Round1A.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <stdio.h>
#include <string>
#include <iostream>
#include <algorithm> 
#include <functional>  
using namespace std;

int main(void) {
	int testcases, firstMethod, secondMethod, N;
	int* values;
	int *min, *max;
	int maxDifference;
	bool flag = true;
	int same;
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	cin >> testcases;	
	for (int i = 1; i <= testcases; i++) {
		firstMethod = 0;
		secondMethod = 0;
		maxDifference = 0;
		cin >> N;
		values = new int[N];
		cin >> values[0];
		same = 0;
		for (int j = 1; j < N; j++) {
			cin >> values[j];
			if (values[j - 1] > values[j]){
				firstMethod += values[j - 1] - values[j];
				if (values[j - 1] - values[j] > maxDifference){
					maxDifference = values[j - 1] - values[j];
				}
			}
			if (values[j] == values[j - 1]){
				same++;
			}
		}
		for (int j = 1; j < N; j++) {
			if (values[j - 1] >= maxDifference){
				secondMethod += maxDifference;
			}
			else {
				secondMethod += values[j - 1];
			}
		}
		if (same == N-1){
			secondMethod = 0;
		}

		cout << "Case #" << i << ": " << firstMethod << " " << secondMethod << endl;
	}
	return 0;
}