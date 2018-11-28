#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int N, M, bil[1010], tot, ans, maks;

	scanf("%d", &N);
	for(int k=0; k<N; k++)
	{
		maks = 0;
		scanf("%d\n", &M);
		for(int i=0; i<M; i++)
		{
			scanf("%d", &bil[i]);
			maks = max(maks, bil[i]);
		}

		ans = maks;
		for(int sisa=1; sisa<=maks; sisa++)
		{
			tot = 0;
			for(int i=0; i<M; i++)
			{
				if(bil[i]%sisa == 0)
					tot += (bil[i] / sisa) - 1;
				else
					tot += (bil[i] / sisa);
			}
			ans = min(ans, tot + sisa);
		}

		printf("Case #%d: %d\n", k+1, ans);
	}
	return 0;
}
