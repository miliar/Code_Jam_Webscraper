#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string.h>

using namespace std;

char c[20], j[20];
int len;
int diff=100000;
char fc[20], fj[20];
int need[20];
void check(int po)
{
	if(po>=len*2)
	{
		int num=0;
		int a=0, b=0;
		for(int i=0;i<len;i++)
		{
			a+=pow(10, len-i-1)*(c[i]-'0');
			b+=pow(10, len-i-1)*(j[i]-'0');
		}
		//printf("%d %d\n", a, b);
		num=abs(a-b);
		if(abs(num)<diff)
		{
			diff=abs(num);
			strcpy(fc, c);
			strcpy(fj, j);
		}
		return;
	}
	if(po<len)
	{
		if(need[po]==1)
		{
			for(int i=0;i<=9;i++)
			{
				c[po]=i+'0';
				check(po+1);
			}
		}
		else
			check(po+1);
	}
	else
	{
		if(need[po]==1)
		{
			for(int i=0;i<=9;i++)
			{
				j[po-len]=i+'0';
				check(po+1);
			}
		}
		else
			check(po+1);
	}
}

int main()
{
	int test_case;
	scanf("%d", &test_case);
	
	for(int ca=1;ca<=test_case;ca++)
	{
		memset(need, 0, sizeof(need));
		scanf("%s %s", c, j);
		len=strlen(c);
		//printf("%d\n", len);
		for(int i=0;i<len;i++)
			if(c[i]=='?')
				need[i]=1;
		
		for(int i=0;i<len;i++)
			if(j[i]=='?')
				need[i+len]=1;
		diff=100000;		
		check(0);
		printf("Case #%d: %s %s\n", ca, fc, fj);
	}
	return 0;
}
