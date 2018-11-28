#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>
#include <iterator>
#include <numeric>

using namespace std;

 int main()
{
	freopen("lottery-small.in","r",stdin);
	freopen("lottery-small.out","w",stdout);

	int T;
	scanf("%d",&T);
	
	int Cas = 1;
	
	long long A, B, K,S ;
	while (T-- >0)
	{
		
		
		scanf("%lld %lld %lld ",&A,&B,&K);
		long long max1 = ::max(A,B);
		long long max2 = ::max(K,max1);
		
		long long i,j;
		S=0;
		for (i=0; i<A;i++)
			for(j=0;j<B;j++)
			{
				if ((i &j )< K)
					S++;
			}


		
		printf("Case #%d: %lld\n",Cas,S);
		
		Cas++;
	}
	return 0;
}