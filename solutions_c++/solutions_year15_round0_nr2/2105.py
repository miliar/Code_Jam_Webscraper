#include<stdio.h>

using namespace std;

int A[1000], N, T;

int main(void)
{
	int l0, l1, l2, l3, curr, ret, wait;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		fprintf(stderr, "%d/%d..\n", l0, T);

		scanf("%d", &N);
		for(l1 = 0; l1 < N; l1++) scanf("%d", &A[l1]);

		ret = A[0];
		for(l1 = 1; l1 < N; l1++) if(A[l1] > ret) ret = A[l1];

		for(wait = 1; wait <= ret; wait++)
		{
			curr = wait;
			for(l1 = 0; l1 < N; l1++)
			{
				if(A[l1] > wait)
				{
					if(A[l1] % wait == 0) curr += (A[l1] / wait) - 1;
					else curr += (A[l1] / wait);
				}
			}
			if(curr < ret) ret = curr;
		}

		printf("Case #%d: %d\n", l0, ret);
	}

	return 0;
}
