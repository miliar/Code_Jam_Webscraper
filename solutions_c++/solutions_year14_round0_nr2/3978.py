#include <cstdio>
using namespace std;
int main(int argc, char const *argv[])
{
	int k=1,t,i;
	double C,F,X;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lf%lf%lf",&C,&F,&X);

		double t1;
		t1=0;
		double x=2.0;
		while(X/x>(C/x+X/(F+x)))
		{
			t1+=C/x;
			x+=F;
		}
		t1+=X/x;
		printf("Case #%d: %.7lf\n",k,t1);
		k++;
	}
	return 0;
}