#include <cstdio>
#include <algorithm>

int main()
{
	int caseT;
	double C,F,X,in,ans,t;
	scanf("%d",&caseT);
	for(int casenum=1;casenum<=caseT;casenum++)
	{
		printf("Case #%d: ",casenum);
		scanf("%lf%lf%lf",&C,&F,&X);
		in=2.0;
		t=0.0;
		ans=X/in;
		for(int i=1;i<=100000;i++)
		{
			t+=C/in;
			in+=F;
			ans=std::min(ans,t+X/in);
		}
		printf("%.7f\n",ans);
	}
	return 0;
}
