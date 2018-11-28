#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int t,tt,n,m;
int a[110][110];
int mx[110];
int my[110];

void work()
{
	scanf("%d%d",&n,&m);
	for (int i=1;i<=n;++i)
		for (int j=1;j<=m;++j) scanf("%d",&a[i][j]);
	
	for (int i=1;i<=n;++i)
	{
		mx[i]=a[i][1];
		for (int j=2;j<=m;++j) mx[i]=max(mx[i],a[i][j]); 
	}	
	
	for (int j=1;j<=m;++j)
	{
		my[j]=a[1][j];
		for (int i=2;i<=n;++i) my[j]=max(my[j],a[i][j]); 
	}	
	
	bool bb=true;
	for (int i=1;i<=n;++i)
		for (int j=1;j<=m;++j)
			if (a[i][j]<mx[i]&&a[i][j]<my[j]) bb=false;
	
	if (bb) printf("Case #%d: YES\n",tt);
	else printf("Case #%d: NO\n",tt);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);


	scanf("%d",&t);
	for (tt=1;tt<=t;++tt) 
	{
		work();
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
