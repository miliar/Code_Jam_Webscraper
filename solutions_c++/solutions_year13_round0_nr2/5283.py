/*
 * main.cpp
 *
 *  Created on: Apr 12, 2013
 *      Author: steven
 */
#include <fstream>
#include <iostream>
using namespace std;

int minimum(int a, int b) {
	if (a < b) return a;
	return b;
}

int main() {
	ifstream f;
	ofstream o;
	o.open("/home/steven/workspace/cj/outB");
	f.open("/home/steven/workspace/cj/inB");
	if (!f.good()) return -1;

	int cases;
	int N;
	int M;
	int **pattern;
	int *columnM;
	int *rowM;

	f >> cases;
	int *ans = new int[cases];
	for (int i = 0; i < cases; i++) {
		ans[i] = true;
	}
	int max;
	for (int step = 0; step < cases; step++) {
		//input
		f >> N;
		f >> M;
		pattern = new int* [N];
		rowM = new int[N];
		columnM = new int[M];
		for (int i = 0; i < N; i++) {
			pattern[i] = new int[M];
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				f >> pattern[i][j];
			}
		}
		//find max of each row
		for (int i = 0; i < N; i++) {
			max = pattern[i][0];
			for (int j = 1; j < M; j++) {
				if (max < pattern[i][j]) max = pattern[i][j];
			}
			rowM[i] = max;
		}
		//find max of each column
		for (int j = 0; j < M; j++) {
			max = pattern[0][j];
			for (int i = 1; i < N; i++) {
				if (max < pattern[i][j]) max = pattern[i][j];
			}
			columnM[j] = max;
		}
		//if minimum(rowMax[row],columnMax[column])
		//is less than row,column then can't be done
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (pattern[i][j]!=minimum(columnM[j],rowM[i])) {
					ans[step]=false;
					break;
				}
			}
			if (ans[step]==false) break;
		}
		//free case specific stuff
		for (int i = 0; i < N; i++) {
			delete[] pattern[i];
		}
		delete[] pattern;
		delete[] rowM;
		delete[] columnM;
	}

	//output stuff
	for (int i = 0; i < cases; i++) {
		if (ans[i]) {
			o << "Case #" << i+1 << ": YES" << endl;
		} else {
			o << "Case #" << i+1 << ": NO" << endl;
		}
	}
	delete[] ans;
	o.close();
	f.close();
}

