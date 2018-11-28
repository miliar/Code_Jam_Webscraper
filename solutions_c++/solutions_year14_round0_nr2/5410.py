#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int T,i;
double last,C,F,V,X,ans;

int main()
{
	freopen("cookie.in","r",stdin);
	freopen("cookie.out","w",stdout);
	scanf("%d",&T);
	for (int cas = 1;cas <= T;cas ++)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		V = 2;
		last = 0;
		ans = X/V;
		for (int i = 1;;i ++)
		{
			double now = last + C/V;
			V += F;
			if (now + X/V < ans) ans = now + X/V;
			else break;
			last = now;
		}
		printf("Case #%d: %.7f\n",cas,ans);
	}
	return 0;
}
