#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int main()
{
	freopen("cookies.in","r",stdin);
	freopen("cookies.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++)
	{
		double C, F, X;
		scanf("%lf%lf%lf",&C,&F,&X);
		double add(2), t(0);
		while (true)
		{
			double t1=C/add+X/(add+F), t2=X/add;
			if (t2<=t1)
			{
				t+=t2;
				break;
			}
			t+=C/add;
			add+=F;
		}
		printf("Case #%d: %.7f\n",TT,t);
	}
	return 0;
}

