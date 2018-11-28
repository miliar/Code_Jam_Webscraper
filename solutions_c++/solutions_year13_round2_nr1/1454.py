#include <iostream>
#include <algorithm>
using namespace std;

int T, A, N;
int sizes[101];
int currAddOps;

int f(int moteIdx, int currSize, int iter) {
	int ops;
	
	if (iter > N) {
		ops = N;
	} else if (moteIdx == N) {
		ops = 0;
	} else if (currSize > sizes[moteIdx]) {
		ops = f(moteIdx + 1, currSize + sizes[moteIdx], 0);
	} else {
		int addOps = 1 + f(moteIdx, currSize + min(currSize - 1, sizes[moteIdx] - 1), iter + 1);
		int removeOps = N - moteIdx;
		
		ops = min(addOps, removeOps);
	}
	
	return ops;
}

int main(void) {
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> A >> N;
		
		for (int i = 0; i < N; i++) {
			cin >> sizes[i];
		}
		
		sort(sizes, sizes + N);
		cout << "Case #" << t << ": " << (A == 1 ? N : f(0, A, 0)) << endl;
	}
}
