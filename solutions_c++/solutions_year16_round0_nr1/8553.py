#include<stdio.h>

void  main()
{
	freopen("A-large.in","r",stdin);
	FILE * out=fopen("output.txt","w");
	int number[10]={0};
	int T=0,N=0;
	int i=0,j=0,n1=0,n2=0,count=0;

	printf("T: ");
	scanf("%d",&T);
	printf("\n");
	
	for(i=0;i<T;i++)
	{
		printf("N:");
		scanf("%d",&N);
		n1=N;
		n2=N;

		if(N==0)
		{
			fprintf(out,"Case #%d: INSOMNIA \n",i+1);
			continue;
		}
		else
		{
			while(1)
			{
				count=0;
				while(1)
				{
					for(j=0;j<10;j++)
					{
						if(n1%10==j)
							number[j]=number[j]+1;
					}
					n1=n1/10;
					if(n1==0)
						break;
				}
				for(j=0;j<10;j++)
				{
					if(number[j]>0)
						count++;
				}
				if(count==10)
					break;
				
				n2=n2+N;
				n1=n2;
			}
			for(j=0;j<10;j++)
				number[j]=0;

			fprintf(out,"Case #%d: %d \n",i+1,n2);
		}
	}
}




