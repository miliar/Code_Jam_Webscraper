#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

void proc(int caseIdx) {
	int k, c, s;
	scanf("%d %d %d", &k, &c, &s);

	printf("Case #%d:", caseIdx);

	int lmt = (int)ceil((double)k / c);
	if (lmt > s) {
		printf(" IMPOSSIBLE\n");
		return;
	}

	vector<long long> output;
	long long res = 0, coff = 1;
	int cnt = 0;
	for (int p = 0; p < k; ++p) {
		res += coff * (k - 1 - p);
		coff *= k;
		++cnt;

		if (cnt >= c) {
			output.push_back(res);
			res = 0;
			coff = 1;
			cnt = 0;
		}
	}
	if (cnt > 0) {
		output.push_back(res);
		res = 0;
		coff = 1;
		cnt = 0;
	}

	for (long long p : output) {
		printf(" %lld", p + 1);
	}
	printf("\n");
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		proc(i);
	}
	return 0;
}