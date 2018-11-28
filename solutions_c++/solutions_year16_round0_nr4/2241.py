#include <cstdio>
#include <cstring>
#include <algorithm>
#define fo(i,a,b) for (int i = a;i <= b;i ++)

int T,cas,K,C,S;

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	for (scanf("%d",&T);T;T --)
	{
		printf("Case #%d: ",++cas);
		scanf("%d%d%d",&K,&C,&S);
		fo(i,1,S-1) printf("%d ",i);
		printf("%d\n",S);
	}
	return 0;
}
