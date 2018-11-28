#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

long long A,B,Ans;

bool ispal(long long x)
{
	long long i,D[15],n=0;

	while(x)
	{
		D[n++]=x%10;
		x/=10;
	}

	for(i=0;i<n/2;i++)
		if(D[i] != D[n-i-1])
			return false;
	return true;
}

int main()
{
	long long i,j,t,T;

	scanf("%lld",&T);

	for(t=1;t<=T;t++)
	{
		printf("Case #%lld: ",t);

		scanf("%lld %lld",&A,&B);
	

		for(Ans=0 , i=ceil(sqrt(A)) ; i*i <= B ; i++)
			if(ispal(i) && ispal(i*i))
				Ans++;

		printf("%lld\n",Ans);
	}


	return 0;
}
