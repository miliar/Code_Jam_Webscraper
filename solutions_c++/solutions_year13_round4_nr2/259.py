#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

#define mp(a,b) make_pair(a,b)

pair<long long, long long> Naive(int n, int p) {
	int pp[15];
	for (int i = 0; i < 15; ++i) {
		pp[i] = i;
	}
	int mx = 1 << 30, mn = 0;
	do {
		
	} while (next_permutation(pp, pp + n));
	return mp(mx, mn);
}

pair<long long, long long> Solve(long long n, long long p) {
	if (p == 1LL << n) {
		return mp(p - 1, p - 1);
	}
	--p;
	long long mx = 0, mn = 0;
	for (int i = n - 1; i > -1; --i) {
		if (!(p & (1LL << i))) {
			mn = (1LL << (n - i)) - 2;
			break;
		}
	}
	if (p == (1LL << n) - 1) {
		mx = (1LL << n) - 1;
	} else {
		mx = 0;
		int lg = 0;
		++p;
		while (p) {
			++lg;
			p >>= 1;
		}
		--lg;
		while (lg) {
			mx += (1LL << (n - lg));
			--lg;
		}
	}
	return mp(mn, mx);
}

int main() {
	freopen("b_large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d: ", I + 1);
		long long n, p;
		cin >> n >> p;
		pair<long long, long long> par = Solve(n, p);
		cout << par.first << " " << par.second << endl;
	}
	return 0;
}