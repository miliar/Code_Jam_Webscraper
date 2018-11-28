#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t,cc=0;
	long long m;
	long double x,c,ans,f,tt,r;
	scanf("%d",&t);
	while(cc<t)
	{
		cc++;
		scanf("%Lf %Lf %Lf",&c,&f,&x);
		ans=0;
		r=2;
		m=1;
		tt=x*f-c*f;
		while(tt-r*c> 0.0000001)
		{
			ans+=c/r;
			r = 2 + m*f;
			m++;
		}
		ans+=x/r;
		printf("Case #%d: %.7Lf\n",cc,ans);
	}
	return 0;
}