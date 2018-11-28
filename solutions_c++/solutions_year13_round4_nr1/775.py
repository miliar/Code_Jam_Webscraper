#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cassert>

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

#define MOD 1000002013

int n;

void cost(long long &r, int from, int to, int num) {
	r += (((
		((long long)(n - (to - from)) * (to - from)) % MOD + 
		(((long long)(to - from) * ((to - from) + 1)) / 2) % MOD
		) % MOD) * num) % MOD;
	r %= MOD;

	/*
	for (int i = 0; i < (to - from); i++) {
		r += ((long long)(n - i) * num) % MOD;
		r %= MOD;
	}
	*/

	//printf("%d %d %d\n", from, to, num);
	//printf("%d\n", r);
}

int task() {
	int m;
	long long r1 = 0, r2 = 0;
	scanf("%d%d", &n, &m);
	priority_queue<pair<int, pair<int, int> >, vector<pair<int, pair<int, int> > >, greater<pair<int, pair<int, int> > > > t; // asc
	for (int i = 0; i < m; i++) {
		int o, e, p;
		scanf("%d%d%d", &o, &e, &p);
		t.push(make_pair(o, make_pair(e, p)));
		cost(r1, o, e, p);
	}

	priority_queue<pair<int, int> > starts; // desc
	priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > ends; // asc
	while (!ends.empty() || !t.empty()) {
		if (ends.empty() || (!t.empty() && t.top().first <= ends.top().first)) {
			pair<int, pair<int, int> > top = t.top();
			t.pop();

			//printf("start %d %d\n", top.first, top.second);

			starts.push(make_pair(top.first, top.second.second));
			ends.push(top.second);
		} else {
			int p = ends.top().first;
			int l = ends.top().second;
			ends.pop();

			//printf("end %d %d\n", p, l);

			while (l > 0) {
				assert(!starts.empty());
				pair<int, int> top = starts.top();
				starts.pop();

				if (top.second > l) {
					cost(r2, top.first, p, l);
					starts.push(make_pair(top.first, top.second - l));
					l = 0;
				} else {
					cost(r2, top.first, p, top.second);
					l -= top.second;
				}
			}
		}
	}

	return (r1 - r2 + MOD) % MOD;
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		printf("Case #%d: %d\n", i, task());
	}
}

