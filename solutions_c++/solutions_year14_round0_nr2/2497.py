// Google Code Jam 2014
// Author: Avaneesh Rastogi
// Date: 12-04-2014

#include<cstdio>
#define debug printf("DEBUG: On Line #: %d\n", __LINE__);
int main()
{
	int t, caseno = 1;
	scanf("%d", &t);
	double C, F, X;
	while (t--)
	{
		scanf("%lf%lf%lf", &C, &F, &X);
		
		double x = 0, y = 0;
		double min = X/2;
		int n = 0;
		
		while (1)
		{
			x += 1.0/(2+n*F);
			y = X*1.0/(2+(n+1)*F);
			if (C*x + y < min)
				min = C*x + y;
			else
				break;
			n++;
		}
		printf("Case #%d: %.7lf\n",caseno++, min);
	}	
	
	return 0;
}
