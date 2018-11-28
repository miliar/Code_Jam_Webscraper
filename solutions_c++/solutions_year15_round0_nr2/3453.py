#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

bool cmp(const int &a, const int &b) {
	return a > b;
}

int 
calcmov(vector<int> &vec, int expmax) {
	int sum = 0;
	for (int i = 0; i < vec.size(); i++) {
		sum += (vec[i] - 1) / expmax;
	}
	return sum;
}

int
main(void) {
	int T;
	int D;
	vector<int> vec;
	scanf("%d", &T);
	for (int seq = 1; seq <= T; seq++) {
		scanf("%d", &D);
		vec = vector<int>(D, 0);
		for (int i = 0; i < vec.size(); i++) {
			scanf("%d", &vec[i]);
		}
		sort(vec.begin(), vec.end(), cmp);

		int opt = vec[0];

		for (int expmax = opt - 1; expmax >= 1; expmax--) {
			int mov = 0;

			mov = calcmov(vec, expmax);

			opt = min(opt, mov + expmax);
		}
		printf("Case #%d: %d\n", seq, opt);
	}
}
