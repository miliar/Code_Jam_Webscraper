#include <algorithm>
#include <cstdio>
#include <functional>
#include <vector>
#include <cmath>

using std::greater;
using std::merge;
using std::printf;
using std::scanf;
using std::sort;
using std::vector;
using std::sqrt;

const int M = 1000;

static int testcase(int D, vector<short>& P) {
	sort(P.begin(), P.end(), greater<short>());
	int b = P[0];
	for(int n = 2; n < P[0]; ++n) {
		int s = n;
		for(int i = 0; i < D && P[i] > n; ++i)
			s += (P[i] - 1) / n;
		if(s < b)
			b = s;
	}
	return b;
}

static void testcase(int t) {
	int D;
	scanf("%d", &D);
	vector<short> P(D);
	for(int i = 0; i < D; ++i)
		scanf("%hd", &P[i]);
	printf("Case #%d: %d\n", t + 1, testcase(D, P));
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; ++t)
		testcase(t);
}
