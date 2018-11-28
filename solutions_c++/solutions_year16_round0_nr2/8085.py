#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<stdlib.h>
#include<string.h>
void main()
{
	FILE *fp,*f;
	char n[101];
	int nt,i,j,k,count,l;
	fp=fopen("code.txt","r");
	f=fopen("code1.txt","w");

	fscanf(fp,"%d",&nt);
	for(i=0;i<nt;i++)
	{
		fscanf(fp,"%s",n);
		l=strlen(n);
		count=0;
		j=l-1;
		while(j>=0)
		{
				if(n[j]=='-')
				{
						for(k=0;k<j;k++)
						{
							n[k]=(n[k]=='-')?'+':'-';
						}
						count++;
				}
				j--;
		}
		fprintf(f,"Case #%d: %d\n",i+1,count);
	}
	fcloseall();
	
}