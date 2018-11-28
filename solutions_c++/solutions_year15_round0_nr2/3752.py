//============================================================================
// Name        : g.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int getResult(int D, int P[]) {
	int max = P[0];
	for(int i = 0; i < D; i++) {
		if(max < P[i])
			max = P[i];
	}

	int result = max;
	for(int i = 1; i <= max; i++) {
		int t = 0;
		for(int j = 0; j < D; j++) {
			t += (P[j] - 1)/i;
		}
		t += i;
		if(result > t)
			result = t;
	}
	return result;
}

int main() {
	FILE *fp = 0;
	fp = fopen("c:\\B-large.in", "r");
	if(fp == 0)
		cout << "File open error!";
	int lines = 0;
	fscanf(fp, "%d", &lines);

	for(int i = 0; i < lines; i++) {
		int D = 0;
		int P[1000];
		fscanf(fp, "%d", &D);
		for(int j = 0; j < D; j++) {
			fscanf(fp, "%d", P+j);
		}
		cout << "Case #" << i+1 << ": " << getResult(D, P) << endl;
	}

	return 0;
}
