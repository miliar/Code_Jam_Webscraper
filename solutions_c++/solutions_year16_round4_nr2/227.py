#include<bits/stdc++.h>
using namespace std;

int n,m;
double a[205],b[205],s[205][205];

inline double gao(int x)
{
	int i,j;
	for(i=0;i<x;i++)
		b[i]=a[i];
	for(i=0;i<m-x;i++)
		b[x+i]=a[n-1-i];
	memset(s,0,sizeof(s));
	s[0][0]=1.0;
	for(i=0;i<m;i++)
		for(j=0;j<=i;j++)
			s[i+1][j]+=s[i][j]*b[i],s[i+1][j+1]+=s[i][j]*(1-b[i]);
	return s[m][m/2];
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,_,i;
	double s;
	for(scanf("%d",&T),_=1;_<=T;_++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			scanf("%lf",&a[i]);
		sort(a,a+n);
		for(s=i=0;i<=m;i++)
			s=max(s,gao(i));
		printf("Case #%d: %.10f\n",_,s);
	}
	return 0;
}
