#include <cstdio>
#include <algorithm>
using namespace std;

int countones(long long p) {
	int i = 0;
	while (p > 0) {
		if (p & 1) i++;
		p >>= 1;
	}
	return i;
}

long long solve(int n, long long p) {
	if (p == 0) {
		return -1;
	}
	long long twon = (long long)1 << (long long)n;
	if (p == twon) {
		return twon - 1;
	}
	p = twon - p;
	int minOnes = countones(p);
	while (p < twon) {
		minOnes = min(minOnes, countones(p));
		p += (p & (-p));
	}
	return twon - ((long long)1 << (long long)minOnes);
}

int main() {
	int ncases = 0;
	scanf("%d", &ncases);
	for (int i = 1; i <= ncases; i++) {
		int n;
		long long p;
		scanf("%d", &n);
		scanf("%lld", &p);
		long long could = solve(n, p);
		long long must = ((long long)1 << (long long)n) - solve(n, ((long long)1 << (long long)n) - p) - 2;
		printf("Case #%d: %lld %lld\n", i, must, could);
	}
}
