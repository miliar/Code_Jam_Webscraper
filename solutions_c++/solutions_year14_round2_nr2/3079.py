#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>
#include<fstream>
#include<limits.h>
int main()
{
	FILE *f,*fp;
	f=fopen("D:\B-small-attempt1.in","r");
	fp=fopen("D:\hacker.in","w");
	int n=1,T;
	fscanf(f,"%d",&T);
	while(T--)
	{
    int A,B,K;
	fscanf(f,"%d %d %d",&A,&B,&K);
	int i=0,j=0,count=0;
	while(1)
	{
		if((i&j)<K)
		count++;
		i++;
		if(i==A)
		{
			i=0;
			j++;
		}
		if(j==B)
		break;
	}
	fprintf(fp,"Case #%d: %d\n",n++,count);
	
}
fclose(f);
	fclose(fp);
	return 0;
}
