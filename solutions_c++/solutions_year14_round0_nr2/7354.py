#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<set>
#include<string>
using namespace std;
typedef long long lld;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);
		double speed=2;
		double ans=x/speed;
		double T=0;
		for(int i=1;i<=1000000;i++)
		{
			T+=c/speed;
			speed+=f;
			ans=min(ans,T+x/speed);
		}
		printf("Case #%d: %.12f\n",cc,ans);
	}
	return 0;
}
/*
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

 */
