#include <stdio.h>
#include <math.h>


double calTime (double c, double f, double x, double cps)
{
	double t = (c/cps + x/(cps+f));

	if (t >= x/cps)
		return x/cps;

	return (c/cps) + calTime(c,f,x,cps+f);
}


int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);

	int T;
	scanf("%d",&T);
	
	int Cas = 1;

	double C,F,X,S;
	double cps = 2.0;
	while (T-- >0)
	{
		scanf("%Lf %Lf %Lf",&C,&F,&X);
		
		
		S = calTime (C,F,X,2);
		
		
		printf("Case  #%d: %.7Lf\n",Cas,S);
		
		Cas++;
	}
	return 0;
}