#include<stdio.h>
int main()
{
	int T,k,c,s,i=1,j;
	scanf("%d",&T);
	while(i<=T)
	{
		scanf("%d %d %d",&k,&c,&s);
		if(s!=k)
		printf("Case #%d: IMPOSSIBLE",i);
		else
		{
            printf("Case #%d: ",i);  
			for(j=1;j<=s;j++)
			printf("%d ",j);
		}
		printf("\n");
		i++;
	}
	return 0;
}
