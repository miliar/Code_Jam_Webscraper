#include <bits/stdc++.h>
using namespace std;

int N;
double V,X,x[105],r[105];

void init()
{
	scanf("%d%lf%lf",&N,&V,&X);
	for (int i=1; i<=N; i++) scanf("%lf%lf",&r[i],&x[i]);
}

void doit()
{
	if (N==1)
	{
		if (X!=x[1]) {puts("IMPOSSIBLE"); return;}
		printf("%.9lf\n",V/r[1]);
	}
	else if (N==2)
	{
		if (x[1]==x[2])
		{
			if (x[1]!=X) {puts("IMPOSSIBLE"); return;}
			printf("%.9lf\n",V/(r[1]+r[2]));
			return;
		}
		double a=V*(X-x[2])/(x[1]-x[2]),b=V-a;
		if (a<0||a>V||b<0||b>V) {puts("IMPOSSIBLE"); return;}
		printf("%.9lf\n",max(a/r[1],b/r[2]));
	}
}


int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1; i<=T; i++)
	{
		init();
		printf("Case #%d: ",i);
		doit();
	}
	return 0;
}
