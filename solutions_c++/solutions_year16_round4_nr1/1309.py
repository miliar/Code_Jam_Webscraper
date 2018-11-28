#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
using namespace std;

const int MAXN=4107;

int i,j,k,n,m,t,p,r,s,x,y,tcase,xcase;
string ans,ts,ta,tb;
// Rock beats Scissors, Scissors beats Paper, and Paper beats Rock
// pr = p, ps = s, rs = r
bool dfs(int p, int r, int s)
{
	// cout<<"p="<<p<<", "<<"r="<<r<<", "<<"s="<<s<<endl;
	bool res;
	if (p+r<s || p+s<r || r+s<p) return false;
	if (p==1 && r==1 && s==0)
	{
		ans="PR";
		return true;
	}
	if (p==1 && r==0 && s==1)
	{
		ans="PS";
		return true;
	}
	if (p==0 && r==1 && s==1)
	{
		ans="RS";
		return true;
	}
	int pr,ps,rs,t;
	if (p+r==s)
	{
		pr=0;
		ps=p;
		rs=r;
	}
	else if (p+s==r)
	{
		pr=p;
		ps=0;
		rs=s;
	}
	else if (r+s==p)
	{
		pr=r;
		ps=s;
		rs=0;
	}
	else
	{
		t=s-r; // maybe negative
		pr=(p-t)/2;
		ps=(p+t)/2;
		rs=(r+s-p)/2;
	}
	res = dfs(pr, rs, ps);
	if (!res) return false;
	ts=ans;
	ans="";
	for (int i=0;i<ts.length();i++)
	{
		if (ts[i]=='P')
		{
			ans+="PR";
		}
		else if (ts[i]=='S')
		{
			ans+="PS";
		}
		else if (ts[i]=='R')
		{
			ans+="RS";
		}
	}
	return res;
}

void sortAns(int n)
{
	int x,y,l;
	int m=(1<<n);
	for (int i=0;i<n;i++)
	{
		x=(1<<i);
		l=x*2;
		y=m/l;
		ts=ans;
		ans="";
		for (int j=0;j<y;j++)
		{
			ta=ts.substr(j*l,x);
			tb=ts.substr(j*l+x,x);
			if (ta>tb) swap(ta,tb);
			ans+=ta;
			ans+=tb;
		}
	}
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>tcase;
	xcase=0;
	while (xcase<tcase)
	{
		xcase++;
		cout<<"Case #"<<xcase<<": ";
		ans="";
		cin>>n>>r>>p>>s;
		if (dfs(p,r,s))
		{
			sortAns(n);
			cout<<ans<<endl;
		}
		else
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}

