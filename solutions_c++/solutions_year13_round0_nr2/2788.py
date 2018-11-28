#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;
#define forn(i,n) for(int i=0;i<(int)n;i++)
int a[110][110];
int u[110],v[110];
bool solve()
{
	int n,m;
	cin>>n>>m;
	forn(i,n)
		forn(j,m)
		cin>>a[i][j];
	forn(i,n)
	{
		u[i]=0;
		forn(j,m)
			u[i]=max(u[i],a[i][j]);
	}
	forn(j,m)
	{
		v[j]=0;
		forn(i,n)
			v[j]=max(v[j],a[i][j]);
	}
	forn(i,n)
		forn(j,m)
	{
		if(a[i][j]!=min(u[i],v[j]))
		{
			return 0;
		}
	}
	return 1;
}
int main()
{
#define TASK "lawnmower"
	freopen(TASK".in","r",stdin);
	freopen(TASK".out","w",stdout);
	int t;
	cin>>t;
	forn(i,t)
	{
		printf("Case #%d: ",i+1);
		if(solve())
			puts("YES");
		else
			puts("NO");
	}
	return 0;
}