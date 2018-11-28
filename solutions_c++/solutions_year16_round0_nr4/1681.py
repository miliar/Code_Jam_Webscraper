#include <cstdio>

int main()
{
	int T,K,C,S;
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		scanf("%d%d%d",&K,&C,&S);
		for (int j=1;j<=S;j++)
			printf("%d ",j);
		printf("\n");
	}
	return 0;
}