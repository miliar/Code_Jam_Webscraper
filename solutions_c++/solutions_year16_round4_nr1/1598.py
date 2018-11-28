#include <algorithm>
#include <iostream>
#include <cstdio>
#include <list>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

bool bruteh(list<int>& l) {
	//printf("BRUTEH "); for (auto i : l) printf("%d ", i); printf("\n");
	if (l.size() == 1) return true;
	for (auto it = l.begin(); it != l.end();) {
		auto n = next(it);
		if (*n == *it) return false;
		if (!*it && *n == 2 || *n == *it - 1) {
			it = next(n);
			l.erase(n);
		} else {
			l.erase(it);
			it = next(n);
		}
	}
	return bruteh(l);
}

bool brute(int n, int r, int p, int s, list<int>&l) {
	//printf("\tBRUTE %d %d %d %d\n", n, r, p, s); for (auto i : l) printf("%d ", i); printf("\n");
	if (n == 0) {
		list<int> L(l);
		if (bruteh(L)) {
			for (auto i : l) {
				printf("%c", "RPS"[i]);
			}
			return true;
		}
		return false;
	}
	n -= 2;
	// try pr
	if (p && r) {
		--p; l.push_back(1);
		--r; l.push_back(0);
		if (brute(n, r, p, s, l)) return true;
		l.pop_back(); l.pop_back();
		++p;
		++r;
	}
	// try ps
	if (p && s) {
		--p; l.push_back(1);
		--s; l.push_back(2);
		if (brute(n, r, p, s, l)) return true;
		l.pop_back(); l.pop_back();
		++p;
		++s;
	}
	// try rs
	if (r && s) {
		--r; l.push_back(0);
		--s; l.push_back(2);
		if (brute(n, r, p, s, l)) return true;
		l.pop_back(); l.pop_back();
		++r;
		++s;
	}
	return false;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 0; t++ < T;) {
		int N, r, p, s, n = 1;
		scanf("%d%d%d%d", &N, &r, &p, &s);
		list<int> l;
		while (N--) n*=2;
		printf("Case #%d: ", t);
		if (!brute(n, r, p, s, l)) {
			printf("IMPOSSIBLE");
		}
		printf("\n");
		// Strategy is to pick PR, PS, RS, but never same as last one.
		// 3 1 4:
		// PR RS RS SS = fail
		// 1 1 2:
		// PR SS = fail
		// pick biggest two
		// 3 2 3:
		// PR RS PS RS
		// => PSSR
		// => SR
		// => R
		// RS PR RS PS
		// 4 2 2
		// RS PR RS PR = fail
		// 16: 7 4 5
		// RS PR RS PS [422] => if 2 apart by 2
		// 6 4 6
		// RS PR
		// PR RS PR RS
		// PS PS
		// PP
	}
	return 0;
}
