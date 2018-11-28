#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

int divisor(int x, int n) {
	//printf("%d", x);
	ll z = 0;
	ll s = 1;
	while (x > 0) {
		if (x&1) z += s;
		s *= n;
		x >>= 1;
	}
	//printf(" as %d = %lld\n", n, z);
	//for (int i = 3; ((ll)i)*i <= z; i+=2) {
	for (int i = 2; ((ll)i)*i <= z; i++) {
		if (z % i == 0)
			return i;
	}
	return -1;
}

int divisor2(ll x, int n) {
	for (int i = 2; i < 1000; i++) {
		ll y = x;
		int z = 0;
		int s = 1;
		while (y > 0) {
			if (y&1) {
				z = (z + s) % i;
			}
			s = (s * n) % i;
			y >>= 1;
		}
		if (z == 0)
			return i;
	}
	return -1;
}

int main()
{
	int T, N, J;
	scanf("%d%d%d", &T, &N, &J);
	printf("Case #1:\n");
	int c = 0;
	for (ll i = (1LL<<(N-1))+1; i < (1LL<<N); i+=2) {
		//if (__builtin_popcount(i)%2 == 0)
		//continue;
		int d[11];
		fill(d+2, d+11, 2);
		bool ok = true;
		for (int j = 2; j <= 10; j++) {
			d[j] = divisor2(i, j);
			if (d[j] < 0) {
				ok = false;
				break;
			}
		}
		if (ok) {
			for (int j = N-1; j >= 0; j--) {
				printf("%d", (i&(1<<j))?1:0);
			}
			for (int j = 2; j <= 10; j++) {
				printf(" %d", d[j]);
			}
			printf("\n");
			c++;
			if (c == J)
				break;
		}
	}
}
