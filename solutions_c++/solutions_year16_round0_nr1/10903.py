#include<bits/stdc++.h>
using namespace std;
int main()
{
int t,T=1;
scanf("%d",&t);
while(T<=t)
{
	long long c=0,tm,n,N,i=2,j,k,h[11]={0};
	scanf("%lld",&N);
	if(N){n=N;
	while(c!=10)
	{tm=n;
	while(tm)
	{
		if(!h[tm%10])
		c++;
		h[tm%10]=1;
		tm/=10;
	}
	n=N*i;
	i++;
	}
	printf("Case #%d: %lld\n",T,n-N);
	}
	else
	printf("Case #%d: INSOMNIA\n",T);
T++;
}
return 0;
}
