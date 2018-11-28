#include <stdio.h>

int main()
{
	int T;
	int i,j,k,l,temp,first,second,count,answer;
	int c[4];
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);

		scanf("%d",&first);

		for(j=1;j<=4;j++)
		{
			for(k=0;k<4;k++)
			{
				scanf("%d",&temp);
				if(j==first)
					c[k]=temp;
			}
		}
		scanf("%d",&second);
		count = 0;
		for(j=1;j<=4;j++)
		{
			for(k=0;k<4;k++)
			{
				scanf("%d",&temp);
				if(j==second)
				{
					for(l=0;l<4;l++)
					{
						if(c[l]==temp)
						{
							count++;
							answer = temp;
						}
					}
				}
			}
		}

		if(count == 0) printf("Volunteer cheated!\n");
		else if(count == 1) printf("%d\n",answer);
		else printf("Bad magician!\n");
	}
}
