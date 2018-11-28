#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <memory>
#include <map>
#include <queue>
using namespace std;

int Si[1001];

int main(){
	int T;
	int Smax;
	cin >> T;
	for (int testcase = 1; testcase <= T; ++testcase) {
		cin >> Smax;

		char c;
		int total = 0;
		int peopleNeeded = 0;
		for (int i = 0; i <= Smax; i++) {
			cin >> c;
			if (total < i) {
				peopleNeeded++;
				total++;
			}
			Si[i] = c - '0';
			total += Si[i];
		}

		printf("Case #%d: %d\n", testcase, peopleNeeded);
	}
	return 0;
}

int umain() {
	FILE* fptr;
	fopen_s(&fptr, "output.out", "w");
	fstream fin("input.in");

	int T;
	int Smax;
	if (!fin.is_open()) {
		cin >> T;
	}
	fin >> T;
	for (int testcase = 1; testcase <= T; ++testcase) {
		fin >> Smax;

		char c;
		int total = 0;
		int peopleNeeded = 0;
		for (int i = 0; i <= Smax; i++) {
			fin >> c;
			if (total < i) {
				peopleNeeded++;
				total++;
			}
			Si[i] = c - '0';
			total += Si[i];
		}

		fprintf(fptr, "Case #%d: %d\n", testcase, peopleNeeded);
	}
	fclose(fptr);
	return 0;
}