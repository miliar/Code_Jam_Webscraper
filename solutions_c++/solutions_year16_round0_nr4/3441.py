#include <bits/stdc++.h>
using namespace std;

int K,C,S;

void init()
{
	scanf("%d%d%d",&K,&C,&S);
}

void doit()
{
	for (int i=1; i<S; i++) printf("%d ",i);
	printf("%d\n",S);
}

int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1; i<=T; i++)
	{
		init();
		printf("Case #%d: ",i);
		doit();
	}
	return 0;
}
