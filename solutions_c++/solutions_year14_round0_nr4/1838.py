#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

const double eps = 1e-10;

int cmp (const void *a, const void *b) {
	double delta = *(double*)a - *(double*)b;
	if (delta < -eps) {
		return -1;
	} else if (delta > eps) {
		return 1;
	}
	return 0;
}

int solve(int N, double* naomi, double* ken) {
	int score = 0;

	for (int i = 0, j = 0; i < N; i++) {
		while (ken[j] < naomi[i] && j < N) {
			j ++;
		}
		if (j >= N) {
			return N - i;
		}
		j ++;
	}
	return score;
}

int solve_deceitful(int N, double* naomi, double* ken) {
	int score = 0;
	for (int i = 0, j = 0; i < N; i++) {
		if (naomi[i] > ken[j]) {
			score ++;
			j ++; 
		}
	}
	return score;
}

int main() {
	int T, N;
	double naomi[5000], ken[5000];
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		for (int j = 0; j < N; j++) {
			cin >> naomi[j];
		}
		for (int j = 0; j < N; j++) {
			cin >> ken[j];
		}
		qsort(naomi, N, sizeof(double), cmp);
		qsort(ken, N, sizeof(double), cmp);
		int ans1 = solve_deceitful(N, naomi, ken);
		int ans2 = solve(N, naomi, ken);
		cout << "Case #" << (i+1) << ": " << ans1 << " " << ans2 << "\n";
/*		
		for (int j = 0; j < N; j++) {
			cout << naomi[j] << " ";
		}
		cout << endl;
		for (int j = 0; j < N; j++) {
			cout << ken[j] << " ";
		}
		cout << endl;
*/		
	}
	return 0;
}
