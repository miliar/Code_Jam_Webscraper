#include<stdio.h>

void main()
{
	freopen("B-large.in","r",stdin);
	FILE * out=fopen("output.txt","w");
	char pancake[100]={0};
	int T=0;
	int i=0,j=0,k=0,count=0,length=0;

	printf("T:");
	scanf("%d",&T);
	printf("\n");

	for(i=0;i<T;i++)
	{
		length=0;
		count=0;
		printf("pancake:");
		scanf("%s",pancake);

		while(pancake[length]!=0)
			length++;

		for(j=length-1;j>=0;j--)
		{
			if(pancake[j]=='-')
			{
				for(k=j;k>=0;k--)
				{
					if(pancake[k]=='+')
						pancake[k]='-';
					else if(pancake[k]=='-')
						pancake[k]='+';
				}
				count++;
			}
		}

		fprintf(out,"Case #%d: %d \n",i+1,count);
	}
}


