#include <stdio.h>
#include <algorithm>

using namespace std;

int A[1001];

int main()
{
	int T, i, j, N;
	long long f=0, s=0;
	int mmax=0;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d", &T);

	

	for(i=1; i<=T; i++)
	{
		f=0;
		s=0;
		mmax=0;
		scanf("%d", &N);

		scanf("%d", &A[0]);

		for(j=1; j<N; j++)
		{
			scanf("%d", &A[j]);
			
			if(A[j]<A[j-1])
				f+=(A[j-1]-A[j]);
			mmax=max(mmax, A[j-1]-A[j]);
		}
		
		mmax=max(mmax, 0);

		for(j=0; j<N-1; j++)
		{
			if(A[j]<=mmax)
				s+=A[j];
			else
				s+=mmax;
		}

			printf("Case #%d: %lld %lld\n", i, f, s);
	}
		

	return 0;
}