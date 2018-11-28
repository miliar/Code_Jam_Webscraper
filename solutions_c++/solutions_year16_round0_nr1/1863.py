// QA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdio.h>
#include <unordered_set>

using namespace std;

int gcd(int a, int b) {
	return b == 0 ? a : gcd(b, a % b);
}

bool isSetComplete(unordered_set<int>& digits) {
	for (int i = 0; i < 10; i++) {
		if (digits.find(i) == digits.end()) {
			return false;
		}
	}
	return true;
}

int solve(int N) {
	if (N == 0) {
		return -1;
	}

	int r = 0;
	unordered_set<int> digits;

	int iter = 0;
	while (!isSetComplete(digits)) {

		if (iter > 1000000) {
			return -1;
		}

		r += N;
		int n = r;
		while (n > 0) {
			digits.insert(n % 10);
			n /= 10;
		}
	}
	return r;
}

int main()
{
	int nTestCases, N;

	FILE *fin = fopen("A-large.in", "r"); if (!fin) { printf("Couldn't open input file!!!!\n"); return 0; }
	FILE *fout = fopen("large.out", "w");

	fscanf(fin, "%d", &nTestCases);
	for (int testCase = 1; testCase <= nTestCases; testCase++) {
		fscanf(fin, "%d", &N);
		int r = solve(N);
		if (r > 0) {
			fprintf(fout, "Case #%d: %d\n", testCase, r);
			printf("Case #%d: %d\n", testCase, r);
		}
		else {
			fprintf(fout, "Case #%d: INSOMNIA\n", testCase);
			printf("Case #%d: INSOMNIA\n", testCase);
		}
	}

	fclose(fin);
	fclose(fout);
    
	getchar();
	return 0;
}

