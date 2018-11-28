#include <iostream> 
#include <algorithm> 

using namespace std;

static double solve( )
{
	double C; cin>>C;
	double F; cin>>F;
	double X; cin>>X;

	double ans=X/2.0;
	double A0=0.0;
	long i=1;

	while(i<10000)
	{
		double temp, A1;
		A1 = A0 + C/(2+(i-1)*F);
		temp = X/(2+i*F)+A1;
		ans = min(ans, temp);
		A0 = A1;
		++i;
	}

	return ans;
};

void main()
{
	int T;	cin>>T;
	for (int case_no=1; case_no<=T; ++case_no )
		printf("Case #%d: %.7lf\n",case_no, solve());
}
