#include <cstdio>
#include <algorithm>
#include <string>
#include <stdint.h>
#include <map>

using namespace std;

const int MOD = 1000002013;

inline int64_t ticket_price(int n, int o, int e, int p) {
	e -= o; o = 2 * n + 1 - e;
	return (int64_t)e * o / 2 * p;
}

int get_result() {
	int tot_should = 0;

	map<int, int64_t> enter, leave;
	int n, m;
	scanf("%d%d\n", &n, &m);
	for (int i = 0; i < m; ++i) {
		int o, e, p;
		scanf("%d%d%d\n", &o, &e, &p);

		tot_should += ticket_price(n, o, e, p) % MOD;
		tot_should %= MOD;

		enter[o] += p;
		leave[e] += p;
	}

	fprintf(stderr, "ticket price for dist 0, 1, n - 1: %ld, %ld, %ld\n",
		ticket_price(n, 0, 0, 1), ticket_price(n, 0, 1, 1),
		ticket_price(n, 0, n - 1, 1));

	int tot_actual = 0;
	map<int, int64_t>::iterator leave_it, leave_end = leave.end(),
		enter_it;
	for (leave_it = leave.begin(); leave_it != leave_end; ++leave_it) {
		int e = leave_it->first;
		int64_t p = leave_it->second;
		int64_t d;

		fprintf(stderr, "%ld people leave at %d\n", p, e);

		while (p > 0) {
			enter_it = enter.upper_bound(e);
			--enter_it;
			d = min(p, enter_it->second);

			tot_actual += ticket_price(n, enter_it->first, e, d)
				% MOD;
			tot_actual %= MOD;
			p -= d;
			if (p > 0)
				enter.erase(enter_it);
			else
				enter_it->second -= d;
		}
	}

	return (tot_should - tot_actual + MOD) % MOD;
}

int main() {
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i)
		printf("Case #%d: %d\n", i + 1, get_result());
	return 0;
}
