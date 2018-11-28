#include<stdio.h>

int main()
{
	int n,s,sm,num;
	FILE *fp1,*fp2;
	fp1=fopen(".//A-large.in","r");
	fp2=fopen(".//A-large.out","w+");	
	fscanf(fp1,"%d",&n);
	printf("n=%d\n",n);
	num=1;
	while(num<=n)
	{
		int sum=0;
		int maxnum=0;
		int minnum=0;
		fscanf(fp1,"%d",&s);
		printf("s==%d\n",s);
		for(int i=0;i<s+1;i++)
		{
			char c;
			fscanf(fp1,"%c",&c);
			//printf("c==%d\n",c);
			if(c==' '){i--;continue;}
			sm=c-'0';
			printf("sm==%d\n",sm);
			if(sum+maxnum<i)
				maxnum=i-sum;
				
			sum+=sm;
		}
		fprintf(fp2,"Case #%d: %d\n",num,maxnum);
		num++;
	}
	return 0;
}
