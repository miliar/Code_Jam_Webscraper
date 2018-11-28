#include<iostream>
#include<stdio.h>
#include<string>
#include<cstdio>
#include <sstream>

using namespace std;

void main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t;cin>>t;
	for(int i=1;i<=t;++i)
	{
		int first; cin>>first;
		
		int f[4][4];
		for(int j=0;j<4;++j)
		{
			for(int k=0;k<4;++k)
				cin>>f[j][k];
		}
		int second;cin>>second;
		
		int s[4][4];
		for(int j=0;j<4;++j)
		{
			for(int k=0;k<4;++k)
				cin>>s[j][k];
		}
		int check=0;
		int po=0;
		for(int j=0;j<4;++j)
		{
			for(int k=0;k<4;++k)
			{
				if(f[first-1][j]==s[second-1][k])
				{check++;po=j;}
			}
		}
		


		cout<<"Case #"<<i<<": ";
		
		if(check==0)
			cout<<"Volunteer cheated!";
		else if(check==1)
			cout<<f[first-1][po];
		else
			cout<<"Bad magician!";
		cout<<endl;

		
		
	}
}
				

