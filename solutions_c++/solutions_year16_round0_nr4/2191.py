#include <iostream>
#include <cstdio>
#include <cstring>

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small.out","w",stdout);
	int T,t;
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		int k,c,s;
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d:",t);
		for (int i=1;i<=s;i++) printf(" %d",i);
		puts("");
	}
	return 0;
}
