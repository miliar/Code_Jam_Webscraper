#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int test, k, c, s;

int main() {
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	scanf("%d", &test);
	for (int uu = 1; uu <= test; uu++) {
		printf("Case #%d:", uu);
		scanf("%d%d%d", &k, &c, &s);
		for (int i = 1; i <= s; i++)
			printf(" %d", i);
		printf("\n");
	}
}
