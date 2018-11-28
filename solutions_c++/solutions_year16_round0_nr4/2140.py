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

void solve()
{
	unsigned n = 0;
	scanf("%u", &n);
	for (unsigned TEST = 0; TEST < n; ++TEST) {
		unsigned C = 0, K = 0, S = 0;
		scanf("%u%u%u", &K, &C, &S);
		printf("Case #%u:", TEST + 1);
		for (unsigned i = 0; i < K; ++i) {
			printf(" %u", i + 1);
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