#include<cstdio>
#include<cmath>
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,cse;
	double C,F,X,r,t;
	scanf("%d",&T);
	for(cse = 1;cse <= T;++cse)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		if(X < C)
		{
			printf("Case #%d: %.7lf\n",cse,X / 2.0);
			continue;
		}
		r = 2.0;
		t = C / r;
		while(C *(r + F) < F * X)
		{
			r += F;
			t += C / r;
		}
		t += (X - C) / r;
		printf("Case #%d: %.7lf\n",cse,t);
	}
	return 0;
}
