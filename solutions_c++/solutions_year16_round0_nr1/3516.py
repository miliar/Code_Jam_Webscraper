//#include<iostream>
#include<algorithm>
#include<math.h>
#include<cstdio>
#include<set>

using namespace std;

set<int> digits;

void add(long long X)
{
	do
	{
		digits.insert(X%10);
		X/=10;
	}while(X >0);
}


long long solve(long long N)
{
	long long W;
	W=N;
	digits.clear();
	add(N);
	while(digits.size() < 10 )
	{
		N+=W;
		add(N);
	}
	return N;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int test =1; test <= t; ++test)
	{
		long long N;
		scanf("%lld", &N);
		if(N==0)printf("Case #%d: INSOMNIA\n", test);
		else printf("Case #%d: %lld\n", test, solve(N));
	}
	/*
	for(int i=125; i<126; ++i)
	{
		printf("%d: %lld\n", i, solve(i));
	}*/
	return 0;
}
