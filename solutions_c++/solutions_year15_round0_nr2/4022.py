#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
	void print(int *P, int D) {
		for (int i = 0; i < D; i++) printf("#%d ", P[i]); printf("\n");
	}
	const static int DMAX = 1000+10;
	int get_fastest(int *P, int D) {
		int idx, time_count;
		sort(P, P+D);
//		print (P, D);
		int global_leastest = P[D-1];
		for (int leastest = P[D-1]; leastest >= 1; leastest--) {
			time_count = 0; int current_longest = 0;
			for (idx = D-1; idx >= 0 && P[idx] >= leastest; idx--) {
				int pieces = ceil(P[idx] * 1.0 / leastest);
				time_count += pieces - 1;
				current_longest = max(current_longest, (int) ceil(P[idx] * 1.0 / pieces));
//				printf("leastest: %d, idx: %d, pieces: %d, time_count: %d, current_longest: %d\n", leastest, idx, pieces, time_count, current_longest);
			}
			if (idx >= 0) current_longest = max(current_longest, P[idx]);
			int this_round_time = time_count + current_longest;
			global_leastest = min(global_leastest, this_round_time);
//			printf("## current_longest:%d, global_leastest: %d\n", current_longest, global_leastest);
		}
		return global_leastest;
	}
	void solve() {
		int Tcase, D, P[DMAX];
		scanf("%d", &Tcase);
		for (int i = 1; i <= Tcase; i++) {
			scanf("%d", &D);
			for (int d = 0; d < D; d++) scanf("%d", &P[d]);
			int fastest = get_fastest(P, D);
			printf("Case #%d: %d\n", i, fastest);
		}
	}
};

int main() {
	Solution solution;
	solution.solve();
	return 0;
}
