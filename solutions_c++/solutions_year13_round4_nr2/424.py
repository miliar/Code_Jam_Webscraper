#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <utility>

using namespace std;

int main ()
{
	int T, iT;
	scanf("%d",&T);
	for (iT = 0; iT < T; iT++)
	{
		printf("Case #%d: ",iT+1);
		long long N, P;
		scanf("%I64i %I64i",&N,&P);
		P--;
		long long total = 1LL << N;
		long long L, R, C;
		long long cnt;
		L = 0; R = total-1LL;
		while (R > L)
		{
			C = (L+R+1)/2LL;
			cnt = C;
			long long worst = 0;
			long long i;
			for (i = 0; i < N; i++)
			{
				if (cnt > 0LL)
				{
					worst = worst * 2LL + 1LL;
					cnt--;
					cnt /= 2LL;
				}
				else worst = worst * 2LL;
			}
			if (worst <= P) L = C;
			else R = C-1;
		}
		printf("%I64i ",L);

		L = 0; R = total-1LL;
		while (R > L)
		{
			C = (L+R+1)/2LL;
			cnt = total - C - 1LL;
			long long best = 0;
			long long i;
			for (i = 0; i < N; i++)
			{
				if (cnt > 0LL)
				{
					best = best * 2LL;
					cnt--;
					cnt /= 2LL;
				}
				else best = best * 2LL + 1LL;
			}
			if (best <= P) L = C;
			else R = C-1;
		}
		printf("%I64i\n",L);
	}
	return 0;
}