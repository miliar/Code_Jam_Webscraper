#include <stdio.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		long long n, p;
		scanf("%lld %lld", &n, &p);
		long long tochno, maybe;
		long long L = 0, R = (1LL << n) - 1;
		while(L < R)
		{
			long long C = (L + R + 1) / 2;
			long long pow2 = 0, k = 1;
			for(pow2 = 0, k = 1; k <= C + 1; k *= 2, pow2++);
			pow2--;
			k = 0;
			for(int i = 0; i < pow2; i++)
				k = 2 * k + 1;
			for(int i = pow2; i < n; i++)
				k *= 2;
			if(k < p)
				L = C;
			else
				R = C - 1;
		}
		tochno = R;
		L = 0, R = (1LL << n) - 1;
		while(L < R)
		{
			long long C = (L + R + 1) / 2;
			long long pow2 = 0, k = 1;
			for(pow2 = 0, k = 1; k <= (1LL << n) - C; k *= 2, pow2++);
			pow2--;
			k = 0;
			for(int i = 0; i < pow2; i++)
				k = 2 * k;
			for(int i = pow2; i < n; i++)
				k = 2 * k + 1;
			if(k < p)
				L = C;
			else
				R = C - 1;
		}
		maybe = R;
		printf("Case #%d: %lld %lld\n", t, tochno, maybe);
	}
	return 0;
}