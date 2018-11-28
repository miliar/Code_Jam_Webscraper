#include <stdio.h>
#include <stdlib.h>
#define rep(i,n) for(i=0;i<n;++i)
#define REP(i,s,n) for(i=s;i <n;++i)

int main()
{
	int T, k;
    double cps,time, C, F, X;
	FILE* out = fopen("abc.txt","w");
	scanf("%d", &T);
	if(1 > T || T > 100)
		return 0;

	rep(k,T)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		cps = 2;time = 0;
		while(1)
		{
			if(X/cps >= (C/cps + X/(cps + F)))
			{
				time += (C/cps);
				cps += F;
			}
			else
			{
				fprintf(out,"Case #%d: %.7lf\n", k+1, (X/cps) + time);
				break;
			}
		}
	}

	fclose(out);
	return 0;
}
