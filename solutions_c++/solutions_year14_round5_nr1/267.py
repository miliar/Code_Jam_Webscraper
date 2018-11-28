#include <bits/stdc++.h>
#define all(x) begin(x), end(x)
using namespace std;
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')

void process() {
	int64_t n, p, q, r, s;
	scanf("%ld%ld%ld%ld%ld", &n, &p, &q, &r, &s);
	vector<int64_t> a(n), b(n + 1);
	for (int i = 0; i < n; ++i) {
		a[i] = (i * p + q) % r + s;
	}
	partial_sum(all(a), begin(b) + 1);
	int p2 = 0;
	int64_t best = numeric_limits<int64_t>::max();
	for (int p1 = 0; p1 < n; ++p1) {
		int64_t s0 = b[p1];
		int64_t s1 = b[p2] - b[p1];
		int64_t s2 = b[n] - b[p2];
		best = min(best, max(max(s0, s2), s1));
		while (p2 < n && s1 < s2) {
			s1 += a[p2];
			s2 -= a[p2];
			++p2;
			best = min(best, max(max(s0, s2), s1));
		}
	}
	assert(best >= 0 && best <= b.back());
	printf("%.10lf\n", double(b.back()-best) / double(b.back()));
}

int main() {
	ios_base::sync_with_stdio(false);
	int tcases;
	scanf("%d", &tcases);
	for (int tcase = 1; tcase <= tcases; ++tcase) {
		printf("Case #%d: ", tcase);
		process();
	}
	return 0;
}
