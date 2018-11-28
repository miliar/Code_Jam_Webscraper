#include <iostream>
#include <string>
#include <math.h>

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(v,p,k) for(int v=p;v<=k;v++)

using namespace std;

bool fair(int a)
{
	char s[300];
	sprintf(s,"%d",a);
	int n=strlen(s);
	for(int i=0;i<n;i++)
	{
		if(s[i]!=s[n-1-i])return false;
	}
	return true;
}

bool fair_square(int a)
{
	if(!fair(a))return false;
	double sq=sqrt(a);
	if(sq*sq!=a)return false;
	return fair((int)sq);
}


int main()
{
	int t,min,max,res;
	cin>>t;
	FOR(c,1,t)
	{
		cin>>min;
		cin>>max;
		res=0;
		FOR(a,min,max)
		{
			if(fair_square(a))
			{
				res++;
			}
		}
		printf("Case #%d: %d\n",c,res);
	}
}
