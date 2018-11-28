#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <set>
#include <map>

using namespace std;

void go()
{
	int n;
	cin>>n;
	vector<string> v(n);
	vector<vector<int> > vs(n);
	vector<vector<char> > vc(n);

	for (int i=0;i<n;i++)
	{
		cin>>v[i];
		vc[i].push_back(v[i][0]);
		vs[i].push_back(1);
		for (int j=1;j<v[i].size();j++)
		{
			if (v[i][j]!=v[i][j-1])
			{
				vc[i].push_back(v[i][j]);
				vs[i].push_back(1);
			}
			else
				vs[i].back()++;
		}
	}
	for (int i=1;i<n;i++)
	{
		if (vc[i]!=vc[i-1])
		{
			cout<<"Fegla Won";
			return;
		}
	}
	int sum = 0;
	for (int i=0;i<vs[0].size();i++)
	{
		int gut = 1000*1000*1000;
		for (int cn=1;cn<=100;cn++)
		{
			int sm = 0;
			for (int j=0;j<n;j++)
			{
				sm+=abs(vs[j][i]-cn);
			}
			gut = min(gut,sm);
		}
		sum+=gut;
	}
	cout<<sum;
		
}
int main()
{	
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int cases;
	cin>>cases;
	for (int curcase=1;curcase<=cases;curcase++)
	{
		cout<<"Case #"<<curcase<<": ";
		{
			go();
		}
		cout<<"\n";
	}
	return 0;
}
