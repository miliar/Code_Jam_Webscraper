#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int cases,T,i,j,A,B,K,Count;
	cin>>T;
	for(cases=1;cases<=T;cases++)
	{
		cin>>A>>B>>K;
		Count=0;
		for(i=0;i<A;i++)
			for(j=0;j<B;j++)
				if((i&j) < K)
					Count++;
		printf("Case #%d: %d\n",cases, Count);
	}
	return 0;
}