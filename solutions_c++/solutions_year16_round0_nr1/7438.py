#include <stdio.h>

int check[10];
int sum;
int num,n;

void clr()
{
	for(int i=0;i<=9;i++)
		check[i]=0;
	sum=0;
}

main()
{
	FILE *f=fopen("input.in","r");
	FILE *o=fopen("output.txt","w");
	int test;
	int temp;
	fscanf(f,"%d",&test);
	for(int i=0;i<test;i++)
	{
		fscanf(f,"%d",&num);
		n=num;
		clr();
		while(sum!=10&&n!=0)
		{
			for(int m=10;(n*10)/m!=0;m*=10)
			{
				temp=(n%m-n%(m/10))/(m/10);
				if(check[temp]==0)
					sum++;
				check[temp]=1;
			}
			n+=num;	
		}	
		if(n==0)
			fprintf(o,"Case #%d: INSOMNIA\n",i+1);
		else
			fprintf(o,"Case #%d: %d\n",i+1,n-num);
	}	
}
