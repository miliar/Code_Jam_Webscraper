#include<stdio.h>
int main(void)
{
	int tt;
	FILE *fp1,*fp2;
	fp1=fopen("input.in","r");
	fp2=fopen("output.out","w");
	fscanf(fp1,"%d",&tt);
	for(int pp=1;pp<=tt;pp++)
	{
		int i,j,sum=0,product=1,k,a[10]={100,0,0,0,0,0,0,0,0,0};
		long int num,temp;
	int *p;
	p=a;
	fscanf(fp1,"%ld",&num);
	temp=num;
	for(i=1;i<=100;i++)
	{
		num=temp*i;
		for(;num>0;)
		{
			k=num%10;
			*(p+k)=k;
			num=num/10;
		}
		sum=0;product=1;
		for(j=0;j<10;j++)
		{
			sum+=a[j];
			product*=a[j];
		}
		if(sum==45&&product==0)
		break;
	}
	if(i>=100)
	{
		fprintf(fp2,"case #%d: Insomnia\n",pp);
	}
	else{
	
	fprintf(fp2,"case #%d: %ld\n",pp,temp*i);
}	
	}
	
}
