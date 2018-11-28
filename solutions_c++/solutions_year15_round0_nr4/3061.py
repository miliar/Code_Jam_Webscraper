#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
	int t,n=1;
	scanf("%d",&t);
	while(t--)
	{
		int x,r,c,a=1;
		cin>>x>>r>>c;
		int m=r*c;
		if(x==1)
		a=0;
		if(x==2 && m%2==0)
		a=0;
		if(x==3 && (m==6 || m==12 || m==9))
		a=0;
		if(x==4 && (m==12 || m==16))
		a=0;
		if(a==0)
		printf("Case #%d: GABRIEL\n",n);
		else
		printf("Case #%d: RICHARD\n",n);
		n++;
	}
}