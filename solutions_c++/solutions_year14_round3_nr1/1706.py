#include <cstdio>
#include <cassert>
using namespace std;

#define LLD "lld"

long long gcd(long long a, long long b)
{
	return a ? gcd(b % a, a) : b;
}

void test()
{
	long long a, b;
	scanf("%" LLD "/%" LLD "", &a, &b);
	long long c = gcd(a, b);
	a /= c;
	b /= c;
	int x = b;
	while (x % 2 == 0) x /= 2;
	if (x != 1) {
		printf("impossible");
		return;
	}
	int d = 0;
	while (1) {
		if (a >= b) {
			printf("%i", d);
			return;
		}
		b /= 2;
		d++;
	}
	assert(0);
}

int main()
{
	int t;
	scanf("%i", &t);
	for (int i = 0; i < t; i++) {
		printf("Case #%i: ", i +1);
		test();
		printf("\n");
	}
	return 0;
}

