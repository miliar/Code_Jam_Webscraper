#include <iostream>     // std::cout
#include <algorithm>    // std::next_permutation, std::sort
#include <math.h>
#include <stdlib.h>
#include <stack>
#include <queue>
#include <stdio.h>

using namespace std;


int d;
int p[10000];

void solve(int& nr_iter, int& best) {

	int mmax = 0;
	int j = 0;
	for (int i = 0; i < d; ++i) {
		if (mmax < p[i]) {
			mmax = p[i];
			j = i;
		}
	}

	best = min(best, mmax + nr_iter);

	if (mmax == 3) return;

	nr_iter ++;


	for (int a = max(1,(int) sqrt(p[j])); a <= min(p[j]-1, 2 + (int) sqrt(p[j])); a++) {
		int b = p[j];
		d++;
		p[d - 1] = b - a;
		p[j] = a;
		solve(nr_iter,best);
		d--;
		p[j] = b;
	}

	nr_iter --;
}



int main () {
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		
		cin >> d;
		for (int i = 0; i < d; ++i) {
			cin >> p[i];
		}		


		int nriter = 0;
		int best = 100000;
		solve(nriter, best);

		printf("Case #%d: %d\n", t, best);

	}
	return 0;
}
