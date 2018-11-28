#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#define LL long long

using namespace std;

LL Ans[1000];

void Solve(int K,int C,int S)
{
	if ( S < K )
	{
		printf(" IMPOSSIBLE\n");
		return ;
	}
	for (int i=1;i<=K;++i)
		Ans[i]=i-1;
	for (int j=2;j<=C;++j)
		for (int i=1;i<=K;++i)
			Ans[i]= Ans[i]*K + Ans[i]%K;
	for (int i=1;i<=K;++i)
		printf(" %lld",Ans[i]+1);
	printf("\n");
}

int main()
{
	int T,S,K,C;
	scanf("%d",&T);
	for (int i=1;i<=T;++i)
	{
		scanf("%d%d%d",&K,&C,&S);
		printf("Case #%d:",i);
		Solve(K,C,S);
	}
}



