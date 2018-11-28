#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	FILE *fp;
	fp=fopen("aabeasdytrr.txt","w");
	char c[101];
	int t,i,count,j;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		cin>>c;
		for(j=0,count=0;j<strlen(c)-1;j++)
		{
			if(c[j]!=c[j+1])count++;
			
		}
		if(c[j]=='-')count++;
		fprintf(fp,"Case #%d: %d\n",i,count);
	}
	return 0;
}
