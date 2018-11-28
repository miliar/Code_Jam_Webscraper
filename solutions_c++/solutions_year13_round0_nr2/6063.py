//============================================================================
// Name        : gcj-lm.cpp
// Author      : Yo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

const char* lm(vector< vector <int> > grass, int N, int M) {
	for (int n = 0; n < N; n++) {

		int check = grass[n][0];
		for (int m = 0; m < M; m++) {
			if (check < grass[n][m])
				check = grass[n][m];
		}

		for (int m = 0; m < M; m++) {
			if (check != grass[n][m]) {
				if (check < grass[n][m])
					return "NO";

				for (int o = 0; o < N; o++) {
					if (grass[n][m] != grass[o][m])
						return "NO";
				}
			}
		}
	}

	for (int n = 0; n < M; n++) {

		int check = grass[0][n];
		for (int m = 0; m < N; m++) {
			if (check < grass[m][n])
				check = grass[m][n];
		}

		for (int m = 0; m < N; m++) {
			if (check != grass[m][n]) {
				if (check < grass[m][n])
					return "NO";

				for (int o = 0; o < M; o++) {
					if (grass[m][n] != grass[m][o])
						return "NO";
				}
			}
		}
	}

	return "YES";
}

int main() {
	int n, N, M, t;

	if (cin >> n) {
		for (int i = 0; i < n; i++) {
			vector< vector <int> > test;
			cin >> N;
			cin >> M;

			for (int j = 0; j < N; j++) {
				vector<int> testj;

				for (int k = 0; k < M; k++) {
					cin >> t;
					testj.push_back(t);
				}
				test.push_back(testj);
			}

			cout << "Case #" << (i+1) << ": " << lm(test, N, M) << endl;
		}
	}

	return 0;
}
