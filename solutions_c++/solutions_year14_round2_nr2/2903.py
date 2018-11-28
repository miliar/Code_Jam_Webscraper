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
	int a,b,k;
	int count;
	cin>>t;
	for(int x=1;x<=t;x++)
	{
		cin>>a>>b>>k;
		count=0;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if((i&j)<k)
				{
					//cout<<i<<" "<<j<<"\n";
					count++;
				}
			}
		}
		cout<<"Case #"<<x<<": "<<count<<"\n";
	}
	
	return 0;
}

