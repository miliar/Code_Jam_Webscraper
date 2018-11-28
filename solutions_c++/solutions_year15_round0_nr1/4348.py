/************************************************************************
Author : Rdrocks09
Title : CodeJam 2015 Problem A 
Algo Used: 
*************************************************************************/
#include <stdio.h>

using namespace std;
#define gc getchar_unlocked

int read_int()
{
	register char ch;
	ch=gc();
	while(ch<'0'||ch>'9') ch=gc();
	int ret=0;
	while(ch>='0'&& ch<='9')
	{
		ret=ret*10+ch-48;
		ch=gc();
	}
	return ret;							
} 

long long int read_long_long_int()
{
	register char ch;
	ch=gc();
	while(ch<'0'||ch>'9') ch=gc();
	long long int ret=0;
	while(ch>='0'&& ch<='9')
	{
		ret=ret*10+ch-48;
		ch=gc();
	}
	return ret;							
} 

long int read_long_int()
{
	register char ch;
	ch=gc();
	while(ch<'0'||ch>'9') ch=gc();
	long int ret=0;
	while(ch>='0'&& ch<='9')
	{
		ret=ret*10+ch-48;
		ch=gc();
	}
	return ret;							
} 
int main()
{
	int t=read_int(),smax;
	long long int stand_count,ans;
	register char ch;
	for(int x=1;x<=t;++x)
	{
		ans=0;stand_count=0;
		smax=read_int();
//		scanf("%s",str);
		for(int i=0;i<=smax;++i)
		{
			ch=gc();
			while(ch<'0'||ch>'9') ch=gc();
			if(i>stand_count)
			{
				ans+=(i-stand_count);
				stand_count+=(i-stand_count);
			}
			stand_count+=(int)(ch-'0');
		}
		printf("Case #%d: %lld\n",x,ans);
	}
	return 0;
}
