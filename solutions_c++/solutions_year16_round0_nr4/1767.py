//============================================================================
// Name        : 2016_gcj_d.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

#define RUN

unsigned long long k, c, s;
unsigned long long ans[110];
unsigned int n;

unsigned long long solve(unsigned long long lf, unsigned long long rt) {
	unsigned long long ret = 0;
	unsigned long long x = lf;
	for (unsigned int i = 0; i < c; i++) {
		(ret *= k) += x;
		(x += 1) %= rt;
	}
	return ret;
}

int main() {

#ifdef RUN
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
#endif

	int t;
	unsigned long long tmp;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d:", cas);
		n = 0;
		cin >> k >> c >> s;
		if (s < (k+c-1)/c) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		tmp = 0;
		while (tmp < k) {
			if (tmp+c > k)
				ans[n++] = solve(tmp, k);
			else
				ans[n++] = solve(tmp, tmp+c);
			tmp += c;
		}
		for (unsigned int i = 0; i < n; i++)
			cout << " " << ans[i]+1;
		printf("\n");
	}
	return 0;
}
