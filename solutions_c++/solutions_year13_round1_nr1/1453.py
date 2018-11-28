#include <stdio.h>
#include <math.h>

int main()
{
	int n;
	scanf(" %d",&n);
	for(int i=0; i<n; i++)
	{
		long long int r,t,resp=0;
		scanf(" %lld %lld",&r,&t);
		while(1)
		{
			long long int A = 2*r+1;
			if(t<A) break;
			t-=A;
			r+=2;
			resp++;
		}
		printf("Case #%d: %lld\n",i+1,resp);
	}
	return 0;
}
