#include <bits/stdc++.h>
#define eps 1e-8
using namespace std;
long long V,X;
long long r[2],x[2];
int n;
void sol()
{
	if(n==1)
	{
		if(x[0]==X)
			printf("%.9lf\n",V*1.0/r[0]);
		else
			puts("IMPOSSIBLE");
		return;
	}
	if(x[1]==x[0])
	{
		if(x[0]==X)
			printf("%.9lf\n",V*1.0/(r[0]+r[1]));
		else
			puts("IMPOSSIBLE");
	}
	else if((x[0]<=X && X<=x[1])||(x[1]<=X && X<=x[0]))
	{
		double v[2];
		v[1]=V*(X-x[0])*1.0/(x[1]-x[0]);
		v[0]=V*(X-x[1])*1.0/(x[0]-x[1]);
		printf("%.9lf\n",max(v[0]*1.0/r[0],v[1]*1.0/r[1]));
	}
	else
		puts("IMPOSSIBLE");
}
void rl(long long &x)
{
	int a,b;
	scanf("%d.%d",&a,&b);
	x=10000LL*a+b;
}
int main()
{
	freopen("B-small-attempt3.in","r",stdin);
	freopen("b5.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		scanf("%d",&n);
		rl(V);rl(X);
		for(int i=0;i<n;i++)
		{
			rl(r[i]);
			rl(x[i]);
		}
		printf("Case #%d: ",cas);
		sol();
	}
	return 0;
}
