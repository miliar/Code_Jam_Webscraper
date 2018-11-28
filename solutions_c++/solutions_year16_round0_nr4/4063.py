#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
	int T, k, c, s, cs = 0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d",&k,&c,&s);
		cs++;
		printf("Case #%d:",cs);
		if(s==k)
			for(int i = 1; i<= s; i++)
				printf(" %d",i);
		else
		{

		}
		printf("\n");
	}
	return 0;
}