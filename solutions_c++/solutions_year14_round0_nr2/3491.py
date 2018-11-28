#include <iostream>
#include <cstdio>
#include <climits>
#include <cfloat>

using namespace std;

int main()
{
	int tc, t;
	double c, f, x, tmin, tcur, tprev, tfarm, tfarm_prev, rate;

	scanf("%d",&tc);
	for(t=1; t<=tc; t++)
	{
		scanf("%lf %lf %lf",&c,&f,&x);

		rate=2;
		tfarm = tfarm_prev = 0;
		tcur = tfarm + x/rate;;
		tprev = DBL_MAX;
		while(tcur<tprev)
		{
			tprev = tcur;
			tfarm = tfarm_prev + c/rate;
			rate = rate + f;
			tcur = tfarm + x/rate;
			tfarm_prev = tfarm;
		}
		printf("Case #%d: %.7lf\n",t,tprev);
	}
		
	return 0;
}
