#include <cstdio>

using namespace std;

int main()
{
	int t,T,k,c,s,i;

	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d %d %d",&k,&c,&s);
		printf("Case #%d: ",t);
		for(i=1;i<=k;i++)
			printf("%d ",i);
		printf("\n");
	}
	return 0;
}
