#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

inline bool pal(long long a)
{
	long long  s=0,t=a;

	while(t)
	{
		s= s*10+t%10;
		t/= 10;
	}

	return (s==a);

}
long long Ar[46];

int main()
{
	freopen("a.in","r",stdin );
	freopen("a.out","w",stdout);

	register long long Ans,T,A,B,s=0,i,j;
	
	for(i=1; i<=10000000; ++i)
		if(pal(i) && pal(i*i))
			Ar[++s]= i*i;

	scanf("%lld",&T);

	for(i=1; i<=T; ++i)
	{
		scanf("%lld %lld",&A,&B);

		for(Ans=0,j=1; j<=39; j++)
			if(Ar[j]<=B && Ar[j]>=A)
				++Ans;

		printf("Case #%lld: %lld\n",i,Ans);		
	}
	
	return 0;
}
