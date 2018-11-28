#include<stdio.h>
#include<conio.h>
int main()
{
	int i,a,b,count,t,k;
	FILE *fp,*fp1;
	fp=fopen("input1.in","r");
	fp1=fopen("out.in","w");
	count=0;
	fscanf(fp,"%d\n",&t);
	for(k=0;k<t;k++)
	{
		fscanf(fp,"%d %d\n",&a,&b);
		for(i=0;i<31;i++)
		{
			if(i*i>=a&&i*i<=b)
			{
				if(i*i<10)
				{	
					count++;
				}
				if(i*i==121||i*i==484)
				{	
					count++;
				}
			}
		}
	//	printf("Case #%d %d\n",k+1,count);
		fprintf(fp1,"Case #%d: %d\n",k+1,count);
		count=0;
	}
	getch();
	return 0;
}
