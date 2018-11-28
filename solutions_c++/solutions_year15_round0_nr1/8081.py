#include <stdio.h>

int main()
{
	freopen("./input.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int casT;
	scanf("%d",&casT);
	for(int cas=1;cas<=casT;cas++)
	{
		int sum=0;
		int count=0;
		int shy,shyMax;
		scanf("%d",&shyMax);
		getchar();
		for(int i=0;i<=shyMax;i++)
		{
			shy=getchar()-'0';
			sum=sum+shy;
			//printf("%d %d %d\n",i,count,sum);
			if(shy==0&&sum+count<i+1)
				count=count+1;
		}
		printf("Case #%d: %d\n",cas,count);
	}
	return 0;
}
