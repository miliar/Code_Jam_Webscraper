// Codejam20151.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include  <iostream>
#include<string>
using namespace std;
int main()
{
	freopen( "input.txt","r",stdin);
	freopen( "output.txt","w",stdout);
	int s;
	int t;
	string shyness;
	cin>>t;
	
	for(int x=1;x<=t;x++)
	{
		int count=0,count1=0,num=0;
		cin>>s>>shyness;
		for(int i=0;i<shyness.length();i++)
		{
			
			if(num<i &&(shyness[i]!='0'))
			{
				count+=(i-num);
				num+=count;
			}
			num += shyness[i]-'0';
		}
		cout<<"Case #"<<x<<": "<<count-count1<<"\n";
	}	
	return 0;
}

