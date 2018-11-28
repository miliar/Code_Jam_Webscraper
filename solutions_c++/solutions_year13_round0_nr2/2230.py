#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <iomanip>
using namespace std;

bool is_possible(const vector<vector<int> > &a)
{
	vector<vector<int> > temp(a.size(), vector<int>(a[0].size(),100));
	for (int i=0;i<a.size();i++)
	{
		int curmax = -1;
		for (int j=0;j<a[0].size();j++)
		{
			curmax = max(curmax, a[i][j]);
		}
		for (int j=0;j<a[0].size();j++)
		{
			temp[i][j] = curmax;
		}
	}
	for (int i=0;i<a[0].size();i++)
	{
		int curmax = -1;
		for (int j=0;j<a.size();j++)
		{
			curmax = max(curmax, a[j][i]);
		}
		for (int j=0;j<a.size();j++)
		{
			temp[j][i] = min(temp[j][i],curmax);
		}
	}
	for (int i=0;i<temp.size();i++)
	{
		for (int j=0;j<temp[0].size();j++)
		{
			if (temp[i][j]!=a[i][j])
				return 0;
		}
	}
	return 1;
}
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int test;
	cin>>test;
	for (int curtest =0; curtest < test;curtest++)
	{
		int n,m;
		cin>>n>>m;

		vector<vector<int> > temp(n,vector<int>(m));
		for (int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				cin>>temp[i][j];

		cout<<"Case #"<<curtest +1<<": ";
		if (is_possible(temp))
			cout<<"YES";
		else
			cout<<"NO";
		cout<<"\n";
	}
	
	

	return 0;
}