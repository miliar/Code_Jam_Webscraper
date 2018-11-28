#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <set>
#include <map>
#include <vector>

using namespace std;

const int maxN = 10000 + 10;
int A[maxN];


int main() {
	int T;
	cin >> T;
	for (int tt=1; tt<=T; ++tt) {
		int X, N;
		cin >> N >> X;
		for (int i=0; i<N; ++i)
			cin >> A[i];
		sort(A, A+N);

		int used = 0;
		for (int i=N-1, j=0; i>=j; --i) {
			used++;
			if (i>j && A[i] + A[j] <= X)
				j++;
		}
		cout << "Case #" << tt << ": " << used << endl;
	}
	return 0;
}
