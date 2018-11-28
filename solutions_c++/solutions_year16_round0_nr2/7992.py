#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,i;
	FILE *fp;
	fp=fopen("op2.txt","w");
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		int a,j;
		char s[101];
		scanf("%s",s);
		for(j=1,a=1;s[j]!='\0';j++)
			if(s[j-1]!=s[j])
				a++;
		if(s[j-1]=='+')
			a--;
		fprintf(fp,"Case #%d: %d\n",i,a);
	}
	return 0;
}
