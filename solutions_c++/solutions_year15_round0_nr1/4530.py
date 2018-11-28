#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

class Solution {
public:
	int compute_invite(int Smax, char *shy) {
		int invite_num = 0;
		int current_num = 0;
		for (int i = 0; i <= Smax; i++) {
			// current need: i persons
			if (current_num < i ) {
				invite_num += (i-current_num);
				current_num += (i-current_num) + shy[i]-'0';
			} else {
				current_num += shy[i] - '0';
			}
		}
		return invite_num;
	}
	const static int MaxShy = 1000+10;
	void solve() {
		int Tcase, Smax;
		char shy[MaxShy];
		scanf("%d", &Tcase);
		for (int t = 1; t <= Tcase; t++) {
			scanf("%d %s", &Smax, &shy);
			printf("Case #%d: %d\n", t, compute_invite(Smax, shy));
		}
	}
};

int main() {
	Solution solution;
	solution.solve();
	return 0;
}
