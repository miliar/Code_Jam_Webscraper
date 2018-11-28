#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

typedef long long ll;

bool seen[10];

bool all_seen() {
	for (int i = 0; i < 10; ++i)
		if (!seen[i]) return false;
	return true;
}

int main() {
	freopen("output.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int n;
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", tt);
			continue;
		}
		fill(seen, seen + 10, false);
		int k = 1;
		while (!all_seen()) {
			ll d = 1ll * k * n;
			while (d > 0) {
				seen[d % 10] = true;
				d /= 10;
			}
			++k;
		}
		printf("Case #%d: %lld\n", tt, 1ll * n*(k - 1));
	}
	/*
	fclose(fp);
	freopen("input.txt", "w", stdout);
	printf("100001\n");
	for (int i = 900000; i <= 1000000; ++i)
		printf("%d\n", i);
	*/
	return 0;
}