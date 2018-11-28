#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int T;
double C,F,X;

double Solve(double now=2)
{
	if ( C/now + X/(now+F) < X/now)
		return C/now + Solve(now+F);
	else return X/now;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("lyzout.txt","w",stdout);
	scanf("%d",&T);
	for (int Case=1;Case<=T;Case++)
	{
		printf("Case #%d: ",Case);
		scanf("%lf%lf%lf",&C,&F,&X);
		printf("%.7f\n",Solve());
	}
   return 0;
}
