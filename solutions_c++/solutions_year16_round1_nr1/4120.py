#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<cstring>
using namespace std;
int main()
{
	int t,i;
	FILE *fp;
	fp=fopen("pr1.txt","w");
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		fprintf(fp,"Case #%d: ",i);
		char s[1001],c;
		string a;
		scanf("%s",s);
		int l,j;
		l=strlen(s);
		a=s[0];
		for(j=1;j<l;j++)
		{
			if(s[j]>=a[0])
				a=s[j]+a;
			else
				a=a+s[j];
		}
		for(j=0;j<l;j++)
			s[j]=a[j];
		s[j]='\0';
		fprintf(fp,"%s",s);
		fprintf(fp,"\n");
	}
	return 0;
}
