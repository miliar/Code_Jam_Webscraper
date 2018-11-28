// Codejam1.cpp : Defines the entry point for the console application.
//
//#include "stdafx.h"

#include <iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<iterator>
using namespace std;
int main()
{
	freopen( "input.txt","r",stdin);
	freopen( "output.txt","w",stdout);
	int t;
	double c,x,f,sum,r;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		sum=0;
		r=2;
		cin>>c>>f>>x;
		while(1)
		{
			if(x/r>(c/r+(x/(r+f))))
			{
				sum+=c/r;
				r=r+f;
			}
			else
			{
				sum+=x/r;
				break;
			}
		}

		cout<<"Case #"<<i<<":";
	     printf(" %0.7lf\n", sum);

	}
	
	return 0;
}

