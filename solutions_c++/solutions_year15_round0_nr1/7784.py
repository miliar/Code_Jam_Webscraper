// A.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"

#include<iostream>
#include<cstdio>
#include <string>
using namespace std;

int main()
{
	int t,i,j,k,mx,total,add;
	string desc;
	freopen("A-large.in","r",stdin);
	freopen("out122.txt","w",stdout);
	scanf("%d\n",&t);

	for(k=1;k<=t;k++)
	{
		scanf("%d ",&mx);
		getline(cin, desc);

		total = 0;
		add = 0;
		for(i=1;i<=mx;i++)
		{
			total += desc[i-1] -48;
			if(desc[i]=='0')continue;
			
			int tmp = i - total;
			if(tmp>0)
			{
				total += tmp;
				add += tmp;
			}
		}

		printf("Case #%d: %d\n", k, add);
	}
	return 0;
}

