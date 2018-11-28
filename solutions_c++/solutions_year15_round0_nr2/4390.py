//============================================================================
// Name        : Codejam15.cpp
// Author      : Mahmoud Saleh A. Gawad
// Version     :
// Copyright   : None.
// Description : Codejam'15 Qualification Round.
//============================================================================

#include <bits/stdc++.h>
using namespace std;

int arr[10];
int solve() {

	int res = 0;
	for (int i = 1; i < 10; i++)
		if (arr[i])
			res = i;
	for (int i = 4; i < 10; i++) {
		if (arr[i]) {
			int x = arr[i];
			for (int j = 1; j <= i / 2; j++) {
				arr[j] += x;
				arr[i - j] += x;
				arr[i] = 0;
				res = min(res, x + solve());
				arr[i] = x;
				arr[j] -= x;
				arr[i - j] -= x;
			}
		}
	}
	return res;
}

int main() {
	ifstream in("b.txt");
	ofstream out("b.out");

	int t;
	in >> t;
	for (int tt = 1; tt <= t; tt++) {
		int d;
		in >> d;
		int x;
		memset(arr, 0, sizeof arr);

		for (int i = 0; i < d; i++) {
			in >> x;
			arr[x]++;
		}

		out << "Case #" << tt << ": " << solve() << endl;
	}

	return 0;
}
