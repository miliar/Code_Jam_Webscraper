#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cassert>
using namespace std;

void openFiles() {
	#ifndef ONLINE_JUDGE
		freopen("A-large.in", "rt", stdin);
		freopen("A-large.out", "wt", stdout);
	#endif
}

void solve() {
	int n; scanf("%d ", &n);
	int s = 0, a = 0;
	for (int i = 0; i <= n; i++) {
		char c; scanf("%c ", &c);
		if (c != '0' && s < i) {
			a += i - s;
			s += i - s;
		}
		s += c - '0';
	}
	static int ntest = 0;
	printf("Case #%d: %d\n", ++ntest, a);
}


int main() {
	openFiles();
	int n; scanf("%d ", &n);
	for (int i = 0; i < n; i++) solve();

	return 0;
}
