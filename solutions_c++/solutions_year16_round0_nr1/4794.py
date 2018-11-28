#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <map>
#include <iostream>
using namespace std;
typedef long long lld;

int N;

void input() {
	scanf("%d", &N);
}

void solve(int icase) {
	map<lld, bool> ht;
	bool saw[10] = { false };
	int m = 0;
	lld x = N;
	lld k = 1;
	while (ht.find(x) == ht.end()) {
		lld y = x;
		for (; y; y /= 10) {
			if (!saw[y % 10]) {
				saw[y % 10] = true;
				++m;
			}
		}
		ht[x] = true;
		if (m >= 10) break;
		x = (N * (++k));
	}
	if (m >= 10) {
		printf("Case #%d: %lld\n", icase, x);
	}
	else {
		printf("Case #%d: INSOMNIA\n", icase);
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		input();
		solve(i);
	}
	return 0;
}