#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int T;
double C,F,X;
int main()
{
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		double T=0,ANS=X/2.0,R=2.0;
		while (T+C/R+X/(R+F)<=ANS)
		{
			ANS=T+C/R+X/(R+F);
			T+=C/R;
			R+=F;
			//printf("%lf\n",ANS);
		}
		printf("Case #%d: ",TT);
		printf("%.7lf\n",ANS);
	}
	return 0;
}