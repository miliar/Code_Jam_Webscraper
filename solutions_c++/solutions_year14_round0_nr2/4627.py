#include <cstdio>
typedef unsigned int uint;

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		double C=0.0,F=0.0,X=0.0;
		scanf("%lf%lf%lf",&C,&F,&X);
		double Rn=2.0;
		double tm=X/Rn;
		while(1)
		{
			double Rn1=Rn+F;
			double a=Rn1*C-X*F;
			if(0<=a)
				break;
			double b=Rn*Rn1;
			tm+=a/b;
			Rn=Rn1;
		}
		printf("Case #%u: %.7f\n",t,tm);
	}
}
