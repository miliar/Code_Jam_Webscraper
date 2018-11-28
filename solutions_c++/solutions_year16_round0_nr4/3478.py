#include<cstdio>
int main()
{
	int t,j;
	scanf("%d",&t);
	int i;
	int k,c,s;
	for(i=0;i<t;i++)
	{
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d:\t",i+1);
		for(j=1;j<=k;j++)
			printf("%d ",j);
		printf("\n");
	}
	return 0;
}
