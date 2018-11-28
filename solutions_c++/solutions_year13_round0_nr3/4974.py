#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<iostream>
using namespace std;
int ll,ul;
int func(int num)
{
	int n=num,s=0,rs=0;
	float rt;
	while(n>0)
	{
		int i=n%10;
		s=s*10+i;
		n=n/10;
	}
	rt=sqrt(num);
	if(rt-(int)rt!=0)
	return 0;
	int rot=(int)rt;
	while(rot>0)
	{
		int i=rot%10;
		rs=rs*10+i;
		rot=rot/10;
	}
	if(num==s)
	if((int)rt==rs)
	return 1;	
}
int intch(char ch)
{
	if((int)ch>=48 && (int)ch<=57)
	return ((int)ch-48);
}
int main(void)
{
	int t,test,ans;
	FILE *fp;
	FILE *rf;
	char ch,c[6];
	fp=fopen("C-small-attempt0.in","r");
	fgets(c,5,fp);
	test=atoi(c);
	int rea[test];
	for(t=0;t<test;t++)
	{
		ans=0;
		fscanf(fp,"%d",&ll);
		fscanf(fp,"%d",&ul);
		for(int i=ll;i<=ul;i++)
		if(func(i)==1)
		{
			ans++;
		}	
		rea[t]=ans;
	}
	rf=fopen("ANS3.in","w+");
	for(t=0;t<test;t++)
	{
		fprintf(rf,"Case #%d: %d\n",t+1,rea[t]);
	}
}
