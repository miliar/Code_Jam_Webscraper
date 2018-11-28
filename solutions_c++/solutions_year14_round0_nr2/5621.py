#include <iostream>
#include <cstdio>
#include <climits>
using namespace std;

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	scanf("%d",&T);
	int TT=0;
	while (TT<T)
	{
		++TT;
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double v=2,t=0,ans=x/2;
		while (1)
		{
			t+=c/v;
			v+=f;
			if (t+(x/v)<ans) ans=t+(x/v); else break;
		}
		printf("Case #%d: %.7lf\n",TT,ans);
	}
	return 0;
}