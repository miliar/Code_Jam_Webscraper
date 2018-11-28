#include<iostream>
#include<cstdio>
#include<cmath>
#include<math.h>
#include<cstring>
#include<string>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
using namespace std;

void init()
{
#ifdef MY_TEST_VAR
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
#endif
}


unsigned long long pow(unsigned long long b, unsigned p) {
	if (p == 0) {
		return 1;
	}
	if (p == 1) {
		return b;
	}
	const unsigned long long fix = ((p % 2) ? b : 1);
	const unsigned long long half = pow(b, p / 2);
	return half * half * fix;
}


void solve()
{
	unsigned N = 0, J = 0;
	scanf("1\n%u%u", &N, &J);
	const unsigned shift = N / 2;
	const unsigned free_positions = shift - 2;
	char part[30];
	const unsigned part_len = 30;
	printf("Case #1:\n");
	for (unsigned i = 0; i < J; ++i) {
		for (unsigned j = 0; j < part_len; ++j) {
			part[j] = 0;
		}
		unsigned state = i;
		unsigned pos = 0;
		for (unsigned pos = 0; pos < free_positions; ++pos) {
			part[pos] = '0' + state % 2;
			state /= 2;
		}
		printf("1%*s11%*s1", free_positions, part, free_positions, part);
		for (unsigned base = 2; base <= 10; base++) {
			printf(" %llu", pow(base, shift) + 1);
		}
		printf("\n");
	}
}

int main()
{
	init();
	solve();
	return 0;
}