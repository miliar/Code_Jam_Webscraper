#include <stdio.h>
#include <string.h>
int main()
{
	int T,cas=0;
	freopen("D-small-attempt2.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		int n,k,c;
		scanf("%d%d%d",&n,&k,&c);
		printf("Case #%d: ",++cas);
		for(int i=1;i<=c;i++)
		{
			printf("%d",i);
			if(i==c)printf("\n");
			else printf(" ");
		}
	}
}