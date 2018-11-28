#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int T,A,B,K;
int main()
{
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++)
	{
		scanf("%d%d%d",&A,&B,&K);
		int ans=0;
		for (int i=0;i<A;i++)
			for (int j=0;j<B;j++)
				ans+=((i & j) <K);
		
		printf("Case #%d: %d\n",TT,ans);
	}
	return 0;
}