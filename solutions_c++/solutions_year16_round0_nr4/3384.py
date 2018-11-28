#include<stdio.h>
#include<string.h>
#include<math.h>
#include<list>
#include<map>
#include<stack>
#include<queue>

int main()
{
	int T,K,C,S;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		scanf("%d %d %d",&K,&C,&S);
		printf("Case #%d: ",i+1);
		for(int i=1;i<=K;i++)
			printf("%d ",i);
		printf("\n");
	}
	return 0;
}