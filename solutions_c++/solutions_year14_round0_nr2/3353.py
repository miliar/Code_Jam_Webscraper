#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	int t, cas;
	double c, f, x, ans, tm ,b;
	scanf("%d",&t);
	for (cas = 1; cas <= t; cas++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		ans=0;
		b = 2;
		tm = x / 2;
		while((c/b) + (x/(f+b)) < tm)
		{
			ans += c/b;
			b += f;
			tm = x/b;
		}
		ans += x/b;
		printf("Case #%d: %.7f\n",cas,ans);
	}
	return 0;
}
