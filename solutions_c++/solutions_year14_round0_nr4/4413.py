#include <cstdio>
#include <algorithm>

int main()
{
	int T, N, ANS_A, ANS_B;
	int ia, ib;
	float a[1001], b[1001];
	scanf("%d", &T);
	for (int t=1;t<=T;t++)
	{
		ia = 0;
		ib = 0;
		ANS_A = 0;
		ANS_B = 0;
		scanf("%d", &N);

		for(int n=0;n<N;n++)
			scanf("%f", &a[n]);
		for(int n=0;n<N;n++)
			scanf("%f", &b[n]);

		std::sort(a, a+N);
		std::sort(b, b+N);

		while (ia < N && ib < N)
		{
			if (a[ia] > b[ib])
			{
				ia++;
				ib++;
                ANS_A++;
			}
			else if (a[ia] < b[ib])
			{
				ia++;
			}
		}
		ia = 0;
		ib = 0;
		while (ia < N && ib < N)
		{
			if (b[ib] > a[ia])
			{
				ia++;
				ib++;
				ANS_B++;
			} 
			else if (b[ib] < a[ia])
			{
				ib++;
			}
		}
	printf("Case #%d: %d %d\n", t, ANS_A, N - ANS_B);
	}
}
