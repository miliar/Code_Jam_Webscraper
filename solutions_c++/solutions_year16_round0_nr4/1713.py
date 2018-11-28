#include <string>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;
int n, j;

int main() {
	int tests;
	int k, c, s;
	long long jump;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &tests);

	for (int t = 1; t <= tests; t++) {
		scanf("%d%d%d", &k, &c, &s);

		jump = pow((long long)k, c - 1);

		printf("Case #%d: ", t);

		for (int i = 1; i <= k; i++) {
			printf("%lld ", ((long long)i-1) * jump + 1);
		}

		printf("\n");
	}

	return 0;
}