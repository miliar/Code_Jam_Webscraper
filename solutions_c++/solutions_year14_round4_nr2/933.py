#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <set>
#include <map>
#include <vector>

using namespace std;

const int maxN = 1000 + 10;

int A[maxN];

int main() {

	int T;
	cin >> T;
	for (int tt=1; tt<=T; ++tt) {
		int N;
		cin >> N;
		for (int i=0; i<N; ++i)
			cin >> A[i];

		int moves = 0;
		for (int k=N-1; k>0; --k) {
			int min_index = 0;
			for (int i=1; i<=k; ++i)
				if (A[i] < A[min_index])
					min_index = i;
			moves += min(min_index, k-min_index);
			for (int i=min_index; i<k; ++i)
				A[i] = A[i+1];
		}
		cout << "Case #" << tt << ": " << moves << endl;
	}
	return 0;
}
