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
int d[10];
int a[10];
int b[10];
int used[10];
int n;
int res;
int test()
{
	int st = 0;
	for (int i=0;i<n-1;i++)
	{
		if (st==0)
		{
			if (d[i]<d[i+1])
				continue;
			else
				st = 1;
		}
		else
		{

			if (d[i]>d[i+1])
				continue;
			else
				return 0;
		}
	}
	return 1;
}
int get()
{
	for (int i=0;i<n;i++)
		b[i]=a[i];
	int cres=0;
	for (int i=0;i<n;i++)
	{
		int j;
		for (j=i;j<n;j++)
		{
			if (d[i]==b[j])
			{
				break;
			}
		}
		for (int k=j;k>i;k--)
		{
			swap(b[k],b[k-1]);
			cres++;
		}
	}
	return cres;
}
void dfs(int step)
{
	if (step == n)
	{
		if (test())
		{
			res = min(res, get());
		}
		return ;
	}
	for (int i=0;i<n;i++)
	{
		if (used[i]==0)
		{
			used[i]=1;
			d[step] = a[i];
			dfs(step+1);
			used[i]=0;
		}
	}
}
void go()
{	
	cin>>n;
	for (int i=0;i<n;i++)
		cin>>a[i];
	if (n<=2)
	{
		cout<<0;
		return;
	}
	for (int i=0;i<n;i++)
		used[i]=0;

	res = n*n;
	dfs(0);
	cout<<res;	
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
