#include <cstdio>
#include <cstring>
#include <cstdlib>
double C,F,X;
double Buy(int farm,double X)
{
	double ret=0;
	if (farm>0) ret+=Buy(farm-1,C);
	double produce=farm*F+2;
	ret+=X/produce;
	return ret;
}
void Main()
{
	double Ans=1e11;
	scanf("%lf%lf%lf",&C,&F,&X);
	for (int i=0;true;++i)
	{
		double tmp=Buy(i,X);
		if (tmp<Ans)
		{
			Ans=tmp;
		}else break;
	}
	printf("%.7lf\n",Ans);
}
int main()
{
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;++i)
	{
		printf("Case #%d: ",i);
		Main();
	}
}
