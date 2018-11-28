#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int k, c, s;
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d:", t);
		for (int i = 1; i <= k; ++i)
			printf(" %d", i);
		printf("\n");
	}
	return 0;
}