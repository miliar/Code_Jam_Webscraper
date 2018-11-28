#include <algorithm>
#include <cctype>
#include <chrono>
#include <climits>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <stack>
#include <string>
#include <strstream>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
typedef int64_t i64;
typedef uint64_t u64;
typedef double dbl;

#define NN 30

int t;
int N, R, P, S;
int a[NN];
int total;

string rec(int n, int p, int r, int s)
{
	string a;
	if (n == 1) {
		if (p) a += 'P';
		if (r) a += 'R';
		if (s) a += 'S';
		return a;
	}
	if (p%2 == 0) {
		a = rec(n-1, p/2, (r+1)/2, s/2) + rec(n-1, p/2, r/2, (s+1)/2);
	} else if (r%2 == 0) {
		a = rec(n-1, (p+1)/2, r/2, s/2) + rec(n-1, p/2, r/2, (s+1)/2);
	} else {
		a = rec(n-1, (p+1)/2, r/2, s/2) + rec(n-1, p/2, (r+1)/2, s/2);
	}
	return a;
}

int main() {
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		scanf("%d%d%d%d", &N, &R, &P, &S);
		int U = 1 << N;
		int V = U/3;
		if (R < V || R > V+1 || P < V || P > V+1 || S < V || S > V+1) {
			printf("Case #%d: IMPOSSIBLE\n", ti+1);
			continue;
		}
		auto s = rec(N, P, R, S);
		printf("Case #%d: %s\n", ti+1, s.data());

	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
