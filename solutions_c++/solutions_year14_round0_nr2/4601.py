#include <cstdio>
#include <algorithm>

using namespace std;

double C,F,X;

int main()
{
	//freopen("input1.in","r",stdin);
	//freopen("output1.out","w",stdout);
	
	int Test;
	scanf("%d",&Test);
	for (int ii=1;ii<=Test;++ii)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		double res=X/2.0;
		double V=2.0;
		for (int i=1;;++i)
		{
			double res1=res-X/V+C/V+X/(V+F);
			V=V+F;
			if (res1>=res-1e-7)
				break;
			res=res1;
		}
		printf("Case #%d: %.7lf\n",ii,res);
	}
	
	return 0;
}