#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

int a, b, k, t;

long long solve() {
	long long answer = 0;

	for (int i = 0; i < a; ++i)
		for (int j = 0; j < b; ++j)
			if ((i & j) < k) ++answer;

	return answer;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		scanf("%d%d%d", &a, &b, &k);
		printf("Case #%d: %d\n", i + 1, solve());
	}

	return 0;
}