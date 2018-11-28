/************************************************************************
Author : Rdrocks09
Title : 
Algo Used:
*************************************************************************/
#include <stdio.h>
#include <cmath>

using namespace std;
#define gc getchar_unlocked

int array[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};

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
int value(char c)
{
	if(c=='i')
		return 2;
	if(c=='j')
		return 3;
	if(c=='k')
		return 4;
}
int main()
{
	int t=read_int(),l;
	long int x;
	long long int len;
	char abc[10000];
	int row,col,cnt,ans; 
	for(int x1=1;x1<=t;++x1)
	{
		cnt=0;
		l=read_int();
		x=read_long_int();
		len=x*l;
		scanf("%s",abc);
		row=value(abc[0]);
		for(int i=1;i<len;++i)
		{
			col=value(abc[i%l]);
			ans=array[(int)abs(row)-1][(int)abs(col)-1];
			if(row<0)
			{
				if(ans<0)
					ans=abs(ans);
				else
					ans=0-ans;
			}
			if(cnt==0 && ans==2)
			{
				++cnt;
				row=value(abc[++i%l]);
			}
			else if(cnt==0 && row==2)
			{
				++cnt;
				row=value(abc[i%l]);
			}
			else if(cnt==1 && ans==3)
			{
				cnt++;
				row=value(abc[++i%l]);
			}
			else if(cnt==1 && row==3)
			{
				cnt++;
				row=value(abc[i%l]);
			}
			else
				row=ans;
		}
		if(cnt==2 && (ans==4 || row==4))
			printf("Case #%d: YES\n",x1);
		else
			printf("Case #%d: NO\n",x1);
	}
	return 0;
}
