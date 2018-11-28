#include<stdio.h>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
using namespace std;
#define fr(i,n) for(int i=0;i<n;i++)
#define fo(i,n) for(int i=1;i<=n;i++)
#define fe(i,n) for(__typeof(n.begin()) i=n.begin();i!=n.end();i++)
vector<int>a[2020];
int h[2020],v[2020],o[2020];
int c,n;
void F(int x,vector<int>&b)
{
	if(h[x])
		return;
	h[x]=1;
	b.push_back(x);
	fe(i,a[x])
		F(*i,b);
}
void dfs(int x)
{
	if(o[x])
		return;
	vector<int>b;
	memset(h,0,sizeof h);
	F(x,b);
	sort(b.begin(),b.end());
	fe(i,a[x])
		if(*i!=x)
			dfs(*i);
	o[x]=++c;
}
int l[3000];
int B[3000];
int main()
{
	int t,x,cc=0;
	for(cin>>t;t--;)
	{
		c=0;
		cerr << t << endl;
		cin>>n;
		memset(v,0,sizeof v);
		fr(i,n+5)
			a[i].clear();
		memset(l,0,sizeof l);
		fo(i,n)
		{
			cin>>x;
			if(l[x])
				a[l[x]].push_back(i);
			if(l[x-1])
				a[i].push_back(l[x-1]);
			l[x]=i;
		}
		memset(l,0,sizeof l);
		fo(i,n)
			cin>>B[i];
		for(int i=n;i;i--)
		{
			int x=B[i];
			if(l[x])
				a[l[x]].push_back(i);
			if(l[x-1])
				a[i].push_back(l[x-1]);
			l[x]=i;
		}
		memset(o,0,sizeof o);
		printf("Case #%d:",++cc);
		fo(i,n)
		{
			dfs(i);
			cout << " " << o[i];
		}
		cout << endl;
	}

	return 0; 
}
