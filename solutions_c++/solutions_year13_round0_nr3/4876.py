#include<iostream>
#include<iomanip>
#include<cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <string.h>

using namespace std;
#define f(i,a,b) for (int i = a; i < b; i++ )
#define rf(i,a,b) for (int i = a; i >=b; i-- )

bool pal[1002];
bool square[1002];
bool checkpal(int n)
{
	int rep=0;
	int tmp=n;
	while(tmp!=0)
	{
		rep=rep*10;
		rep=rep+tmp%10;
		tmp=tmp/10;
	}
	if(n==rep)
		return true;
	else
		return false;
}
void pre()
{
	f(i,0,10)
		pal[i]=true;
	f(i,10,1002)
		pal[i]=checkpal(i);
		
	rf(i,1002,0)
	{
		if(pal[i])
		{
			int a=sqrt(i);
			if(i==a*a)
			if(pal[a])
			square[i]=1;
		}
	}
}
int main()
{
	int t,a,b;
    	scanf("%d",&t);
    	pre();
    	for(int q=1;q<=t; q++)
    	{
    		scanf("%d%d",&a,&b);
    		int count=0;
    		for(int i=a;i<=b;i++)
    			if(square[i])
    				count++;
    		printf("Case #%d: %d\n",q,count);
	}
}
