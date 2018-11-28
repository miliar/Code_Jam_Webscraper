#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int Tn;
double C, F, X;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int i,j;

	cin >> Tn;
	for (int T=1;T<=Tn;T++)
	{
		double rate = 2;
		double a = 0;
		double ans = 0;
		
		cin >> C >> F >> X;

		while (true)
		{
			if (a+C>=X)
			{
				ans += (X-a)/rate;
				break;
			}
			a += C;
			ans += C/rate;

			if ((X-a)*F > C*rate)
			{
				a -= C;
				rate += F;
			}
			else
			{
				ans += (X-a)/rate;
				break;
			}
		}

		printf("Case #%d: %.8lf\n",T,ans);
		//cout << "Case #" << T << ": " << ans << endl;

	}
}