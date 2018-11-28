#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	int ca=0;
	while ( t-- )
	{
	    double c,f,x;
		ca++;
		scanf("%lf%lf%lf",&c,&f,&x);
		double s=2;
		double t=0;
		bool ff=true;
		while ( ff==true )
		{
			double t1=0;
			double t2=0;
			t1=c/s+x/(s+f);
			t2=x*1.0/s;
			if ( t1>t2 )
			{
				ff=false;
				t=t+x/s;
			}
			if ( t1<t2 )
			{
				t=t+c/s;
				s=s+f;
			}
			if ( t1==t2 )
			{
				t=t+x/s;
				ff=false;
			}
		}
		printf("Case #%d: %.7f\n",ca,t);
	}
	return 0;
}
