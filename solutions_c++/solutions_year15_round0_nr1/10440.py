#include<iostream>
#include<math.h>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<limits.h>
#include<stack>
#include<queue>
#define gc getchar_unlocked
#include<stdlib.h>
#include<unistd.h>
using namespace std;


void fastWrite(int a)
{
	char snum[20];
	int i=0;
	do
	{
		snum[i++]=a%10+48;
		a=a/10;
	}while(a!=0);
	i=i-1;
	while(i>=0)
	putchar_unlocked(snum[i--]);
	putchar_unlocked('\n');
}

void fastin(int &x)
{
	int sign=1;
	register int a=gc();
	x=0;
	for(;a<48 || a>57;a=gc())
	{
		if(a=='-')
		sign=-1;
	}
	for(;a>47 && a<58;a=gc())
		x=(x<<1)+(x<<3)+a-48;	
	
	x=x*sign;
		
}
void fastin(unsigned long long int &x)
{
	register int a=gc();
	x=0;
	for(;a<48 || a>57;a=gc());
	for(;a>47 && a<58;a=gc())
		x=(x<<1)+(x<<3)+a-48;	
}



int main()
{
	int t,max_shy,min_req,buffer;
	char string[10005];
	fastin(t);
	for(int i=1;i<=t;i++)
	{
		buffer=min_req=0;
		fastin(max_shy);
		scanf("%s",string);
		//cout<<max_shy<<" "<<string;
		if(max_shy==0)
		printf("Case #%d: %d\n",i,min_req);
		else
		{
			buffer+=(string[0]-48);
			for(int j=1;j<=max_shy;j++)
			{
				if(j>buffer && string[j]!='0')
				{
					min_req+=(j-buffer);
					buffer+=(j-buffer);
				}
				buffer+=(string[j]-48);
			}
			printf("Case #%d: %d\n",i,min_req);
		}
	}
}
