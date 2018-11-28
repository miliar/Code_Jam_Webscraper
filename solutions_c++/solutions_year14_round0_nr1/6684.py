// Codejam1.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<iterator>
using namespace std;
int main()
{
	int t,n;
	int a[4][4];
	vector<int>v;
	vector<int>v1;
	vector<int>inter;
	freopen( "input.txt","r",stdin);
	freopen( "output.txt","w",stdout);
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		cin>>n;
		v.clear();
		v1.clear();
		inter.clear();
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
			}

		for(int  j=0;j<4;j++)
			v.push_back(a[n-1][j]);
		cin>>n;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
			}

		for(int  j=0;j<4;j++)
			v1.push_back(a[n-1][j]);
		sort(v.begin(),v.end());
		sort(v1.begin(),v1.end());
		std::vector<int>::iterator it;
		set_intersection(v.begin(),v.end(),v1.begin(),v1.end(),back_inserter(inter));
		
		if(inter.size()==1)
			cout<<"Case #"<<c<<": "<<inter[0];
		else if(inter.size()==0)
		cout<<"Case #"<<c<<": Volunteer cheated!";
		else
			cout<<"Case #"<<c<<": Bad magician!";
		cout<<"\n";
	}
	return 0;
}

