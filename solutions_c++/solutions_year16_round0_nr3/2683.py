#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int n, m, test, a[33], v[33];

int prime(long long j) {
	for (long long i = 2; i * i <= j; i++)
		if (!(j % i)) return i;
	return 0;
}

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	scanf("%d", &test);
	printf("Case #1:\n");
	scanf("%d%d", &n, &m);
	for (int i = 0; i < 1 << (n - 2); i++) {
		bool ok = true;
		for (int q = 2; q <= 10 && ok; q++) {
			long long j = 1;
			for (int k = 0, sx = i; k < n - 2; k++, sx >>= 1)
				j = j * q + (sx & 1), a[k] = sx & 1;
			j = j * q + 1;
			v[q] = prime(j);
			if (!v[q]) ok = false; 
		}
		if (ok) {
			printf("1");
			for (int i = 0; i < n - 2; i++) printf("%d", a[i]);
			printf("1");
			for (int i = 2; i <= 10; i++) printf(" %d", v[i]);
			printf("\n");
			if (!--m) return 0; 
		}
	}
}

		 
