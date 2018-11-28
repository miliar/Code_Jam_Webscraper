#include <cstdio>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int log(int n) {
	if (n==0) return -1;
	int logVal = -1;
	while (n) {
		logVal++;
		n >>= 1;
	}
	return logVal;
}

int calculate (vector<int>& motes, int x, int A) {
	if (x == motes.size()) return 0;
	int result = 0;
	if (motes[x] < A) {
		A += motes[x];
		return calculate(motes, x+1, A);
	} else {
		// deleted the mote
		int r1 = calculate(motes, x+1, A) + 1;
		int r2 = INT_MAX;
		if (A + (A-1) != A) {
			int logval = log((motes[x] - 1) /  (A-1));
			if (logval <= 0){
				r2 = calculate(motes, x, A+(A-1)) + 1;
			} else {
				int n = (1<<logval);
				r2 = calculate(motes, x, (A-1)*n + 1)+ logval;
			}	
		}
		return result + min(r1, r2);
	}
}

int main () {
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		int result = 0;
		int A,N;
		scanf("%d %d", &A, &N);
		vector<int> motes;
		for(int i = 0; i < N; i++) {
			int m;
			scanf("%d", &m);
			motes.push_back(m);
		}

		// sort the motes
		sort(motes.begin(), motes.end());
		result = calculate(motes, 0, A);
		printf("Case #%d: %d\n", t, result);
	}
	return 0;
}
