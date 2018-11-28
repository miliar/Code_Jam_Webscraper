#include <cstdio>
#include <algorithm>

using namespace std;

double min(double a, double b) { return (a < b) ? a : b; }

//[x][y]
int grid[5][5];

int main() {
	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++) {
		int n;
		scanf("%d", &n);

		double naomi[n];
		double ken[n];
		for (int j = 0; j < n; j++) { scanf("%lf", &naomi[j]); }
		for (int j = 0; j < n; j++) { scanf("%lf", &ken[j]); }

		sort(naomi, naomi+n);
		sort(ken, ken+n);
		/*
		printf("------------------\n");
		for (int j = 0; j < n; j++) {
			printf("%.2lf ", naomi[j]);
		}
		printf("\n------------------\n");
				printf("------------------\n");
		for (int j = 0; j < n; j++) {
			printf("%.2lf ", ken[j]);
		}
		printf("\n------------------\n");
*/
		//deceit
		int naomiWin = 0;

		int nIndex = 0;
		int jIndex = 0;
		while (nIndex < n && jIndex < n) {
			if (naomi[nIndex] > ken[jIndex]) {
				//nIndex++;
				jIndex++;
				naomiWin++;
			}
			nIndex++;
		}

		//normal
		int naomiRealWin = 0;
		int kIndex = n-1;
		for (int j = n-1; j >= 0; j--) {
			if (naomi[j] > ken[kIndex]) {
				naomiRealWin++;
			} else kIndex--;
		}

		printf("Case #%d: %d %d\n", i, naomiWin, naomiRealWin);
	}

	return 0;
}