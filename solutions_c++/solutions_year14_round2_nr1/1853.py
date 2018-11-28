#include <fstream>
#include <math.h>
#include <stdio.h>
//#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <stdlib.h> 
#include <set>
#include <queue>
using namespace std;
//#pragma comment(linker, "/STACK:999999999")
#define ll long long
const long long MAXN = 102;
const long double eps=0.00000000001;

typedef vector<long long> lnum;


ifstream cin("input.txt");
ofstream cout("output.txt");


int res(vector <int> x)
{
	int k=x.size();
	int r=0;
	for (int i=0;i<k;i++)
		r+=x[i];
	double ss=double(r)/k;
	int g=int(ss+0.5);
	r=0;
	for (int i=0;i<k;i++)
	{
		r+=abs(x[i]-g);
	}
	return r;

}


int main()
{
	int qq;
	cin>>qq;
	for (int ww=0;ww<qq;ww++)
	{
		int n;
		cin>>n;
		cout<<"Case #"<<ww+1<<": ";
		vector <string> v(n);
		for (int i=0;i<n;i++)
		{
			cin>>v[i];
			v[i]+='@';
		}
		vector < vector <pair <char,int> > > g(n);
		for (int i=0;i<n;i++)
		{
			int z=1;
			for (int j=0;j<v[i].length()-1;j++)
			{
				if (v[i][j]!=v[i][j+1])
				{
					g[i].push_back(make_pair(v[i][j],z));
					z=1;
				}
				else
					z++;
			}
		}
		int f1=0;
		for (int i=1;i<n;i++)
		{
			if (g[i].size()!=g[i-1].size())
				f1=1;
		}
		if (f1==1)
		{
			cout<<"Fegla Won"<<endl;
		}
		else
		{
			int r=0;
			for (int i=0;i<g[0].size();i++)
			{
				vector <int> x;
				x.push_back(g[0][i].second);
				for (int j=1;j<n;j++)
				{
					x.push_back(g[j][i].second);
					if (g[j][i].first!=g[j-1][i].first)
						f1=1;
				}
				r+=res(x);
			}
			if (f1==1)
			{
				cout<<"Fegla Won"<<endl;
			}
			else
			{
				cout<<r<<endl;
			}
		}
	}
	return 0;




	
	


}