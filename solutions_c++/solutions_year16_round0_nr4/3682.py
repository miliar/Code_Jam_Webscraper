#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	
	int K,C,S;
		
	for (int rr=1;rr<=t;rr++)
	{
		printf("Case #%d:",rr);
	
		scanf("%d%d%d",&K,&C,&S);
		for (int i=1; i<=K; i++)
			printf(" %d",i);
		printf("\n");
	}
	return 0;
}