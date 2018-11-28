#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int K, C, S;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("dataD.out","w",stdout);
	int T, ys = 0;
	scanf("%d", &T);
	while (T--)
	{
		printf("Case #%d: ", ++ys);
		scanf("%d%d%d", &K, &C, &S);
		for (int i = 0; i < K; ++i)
		{
			long long x = i;
			for (int j = 0; j < C - 1; ++j)
			{
				x *= K;
				// printf("x %lld\n", x);
			}
				
			printf("%lld%c", x + 1, i + 1 == K ? '\n' : ' ');
		}

	}

	return 0;
}