// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
using namespace std;


bool Katit(vector <vector< int> > mas,int x,int y )
{
	bool one=true,two=true;
	for(int i=0;i<mas[0].size();++i)
	{
		if(mas[x][i]==2)
		{
			one=false;
			break;
		}
	}
	for(int i=0;i<mas.size();++i)
	{
		if(mas[i][y]==2)
		{
			two=false;
			break;
		}
	}
	return one|two;
}


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	vector<vector<int>> v;
	cin>>T;
	for(int k=1;k<=T;++k)
	{
		bool haveAnsw=false;
		int N,M;
		v.clear();
		cin>>N>>M;
		v.resize(N);
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j)
			{
				int r;
				cin>>r;
				v[i].push_back(r);
			}
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j)
			{
				if(v[i][j]==1 && !Katit(v,i,j) && !haveAnsw)
				{
					cout<<"Case #"<<k<<": NO"<<endl;
					haveAnsw=true;
				}
			}
			if(!haveAnsw)
				cout<<"Case #"<<k<<": YES"<<endl;
	}


	return 0;
}

