#include <iostream>
#include <vector>

using namespace std;

int main()
{
	double C,F,X;
	int T;
	cin>>T;
	for (int tt = 1; tt <= T; ++tt)
	{
		cin>>C>>F>>X;

		double ans = 0;
		double fcount = 0;
		int cookies = 0;
		for (int i = 0; i < X && ans<X/2 ; ++i)
		{
			double usingFarm = C/(fcount*F + 2.0) + X/((fcount+1) * F + 2.0);
			double usingCookies = X/(fcount*F + 2);

			if(usingFarm <= usingCookies) {
				ans += C/(fcount*F + 2.0);
				fcount += 1.0;
			} else {
				ans += usingCookies;
				break;
			}
		}
		ans = min(ans, X/2.0);
		printf("Case #%d: %.7f\n",tt, ans);
	}
	return 0;
}