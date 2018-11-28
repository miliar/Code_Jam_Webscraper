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
const char s = '.';
const char u = '^';
const char d = 'v';
const char r = '>';
const char l = '<';
int n,m;
int used[100][100];
bool Try(const vector<string> & v, int i,int j, int & lasti, int & lastj)
{
	memset(used, 0, sizeof(used));
	int curd = s;
	lasti = -1;
	lastj = -1;
	while (true)
	{
		char curpos = v[i][j];
		if (curpos != s)
		{
			if (used[i][j])
				return true;
			used[i][j] = true;
			curd = curpos;
			lasti = i;
			lastj = j;
		}
		if (curd==s)
			return true;
		else if (curd == u)
			i--;
		else if (curd == d)
			i++;
		else if (curd == r)
			j++;
		else if (curd == l)
			j--;
		if ( i == -1 || i == n ||  j == -1 || j == m)
			return false;
	}
}
void go()
{
	cin>>n>>m;
	vector<string> v(n);
	for (int i=0;i<n;i++)
	{
		cin>>v[i];
	}
	set<pair<int,int> > st;
	for (int i=0;i<n;i++)
	{
		for (int j=0;j<m;j++)
		{
			int ci,cj;
			if (!Try(v,i,j,ci,cj))
			{
				st.insert(make_pair(ci,cj));
			}
		}
	}

	set<pair<int,int> > fixed;
	for (int i=0;i<n;i++)
	{
		for (int j=0;j<m;j++)
		{
			if (v[i][j] != s && st.find(make_pair(i,j)) == st.end())
			{
				fixed.insert(make_pair(i,j));
			}
		}
	}
	int res = 0;
	for (set<pair<int,int> >::iterator it = st.begin(); it != st.end(); it++)
	{
		int ci = it->first;
		int cj = it->second;
		if (fixed.find(*it) != fixed.end())
			continue;

		int q = 0;
		for (int i=0;i<n && q!=2;i++)
		{
			if (i == ci)
				continue;
			if (v[i][cj] != s)
			{
				if (fixed.find(make_pair(i,cj)) != fixed.end())
					q = max(1,q);
				else
				{
					q = 2;
					fixed.insert(make_pair(ci,cj));
					fixed.insert(make_pair(i,cj));
				}
			}	
		}
		for (int j=0;j<m && q != 2;j++)
		{
			if (j == cj)
				continue;
			if (v[ci][j] != s)
			{
				if (fixed.find(make_pair(ci,j)) != fixed.end())
					q = max(1,q);
				else
				{
					q = 2;
					fixed.insert(make_pair(ci,cj));
					fixed.insert(make_pair(ci,j));
				}
			}
		}
		if (q==1)
		{
			res++;
			fixed.insert(make_pair(ci,cj));
		}
		if (q==0)
		{
			cout<<"IMPOSSIBLE";
			return ;
		}
		if (q==2)
		{
			res +=2;
		}
	}
	cout<<res;
}
int main()
{	
	freopen("A-large(2).in","r",stdin);
	freopen("2.out","w",stdout);
	int cases;
	cin>>cases;
	for (int curcase=1;curcase<=cases;curcase++)
	{
		cout<<"Case #"<<curcase<<": ";
		{
			go();
		}
		if (curcase!=cases)
			cout<<"\n";
	}
	return 0;
}
