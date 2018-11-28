/*
author:arushi
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
	string a;
	int t,num=0;
	scanf("%d",&t);
	while(t--)
	{
		cin>>a;
		num++;
		string x="";
		x=x+a[0];
		for(int i=1;i<(int)a.size();i++)
		{
			if(a[i]<x[0])
				x=x+a[i];
			else
				x=a[i]+x;
		}
		cout<<"Case #"<<num<<": "<<x<<"\n";
	}
	return 0;	
}