#include<cstdio>
#include<cstdlib>
#include<set>
using namespace std;

set<double> S;
set<double> ::iterator it;

int main()
{
	int t,T;
	double c,f,x,ans;
	scanf("%d",&T);

	for(t=1;t<=T;t++)
	{
		S.clear();
		scanf("%lf %lf %lf",&c,&f,&x);
		ans = 0.0;
		double i = 2.0;
		while(1)
		{
			double s1 = (double)c/i;
			double s2 = (double)x/i;
			if ( S.size()>0 && *(S.begin()) < (ans+s1))
			{
				break;
			}
			else
			{
				S.insert(ans+s2);
				ans = ans + s1;
				i = i+f;
			}
		}
		
		double ans = *(S.begin());
		
		printf("Case #%d: %.7lf\n",t,ans);
		
	}
	return 0;
}