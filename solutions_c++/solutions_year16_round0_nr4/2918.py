//#include<iostream>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#include<cstring>
#include<set>

using namespace std;



int main()
{
	int t;
	scanf("%d",&t);
	for(int ca=1; ca<=t; ++ca)
	{
		long long K, C, S;
		scanf("%lld %lld %lld", &K, &C, &S);
		printf("Case #%d: ", ca);
		long long border=1;
		for( int i=0; i<C; ++i)
			border*=K;
		long long JUMP = 0;
		for(int i=0; i<K;++i)
		{
			printf("%lld ", JUMP+1);
			JUMP += border/K;
		}
		printf("\n");
		
	}
	
	return 0;
}
