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
	for (unsigned T = 0; T < n; ++T) {
		unsigned answer = 0;
		char line[1000];
		scanf("%500s", line);
		unsigned l = strlen(line);
		for (unsigned i = 0; i + 1 < l; ++i) {
			if (line[i] != line[i + 1]) {
				++answer;
			}
		}
		if (line[l - 1] == '-') {
			++answer;
		}
		printf("Case #%u: %u\n", T + 1, answer);
	}
}

int main()
{
	init();
	solve();
	return 0;
}