//============================================================================
// Name        : DeceitfulWar.cpp
// Author      : J.Son
// Version     :
// Copyright   : GNU LGPL
// Description : 2014 Google Code Jam Qualification Round Problem D
//============================================================================

#include <cstdio>
#include <algorithm>

#define N 1000

using namespace std;

double naomi[N], ken[N];

void readBlocks(double *arr, int n) {
	for (int i = 0; i < n; i++) {
		scanf("%lf", &arr[i]);
	}
}

int main() {
	int maxCaseNum;

	scanf("%d", &maxCaseNum);

	for (int cases = 1; cases <= maxCaseNum; cases++) {
		int n = 0;

		scanf("%d", &n);

		readBlocks(naomi, n);
		readBlocks(ken, n);

		sort(naomi, naomi + n);
		sort(ken, ken + n);

		int naomiDP = 0, kenDP = 0, dAns = 0;
		while (naomiDP < n && kenDP < n) {
			if (naomi[naomiDP] > ken[kenDP]) {
				kenDP++;
			}
			naomiDP++;
		}
		dAns = kenDP;


		int naomiP = 0, kenP = 0, ans = 0;
		while (naomiP < n && kenP < n) {
			if (naomi[naomiP] < ken[kenP]) {
				naomiP++;
			}
			kenP++;
		}
		ans = n - naomiP;

		printf("Case #%d: %d %d\n", cases, dAns, ans);
	}

	return 0;
}
